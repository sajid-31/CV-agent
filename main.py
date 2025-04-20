from gmail_integration.auth import get_gmail_service
from gmail_integration.fetch_emails import fetch_unread_emails
from gmail_integration.send_emails import send_email
from db.actions import save_email_to_db, email_exists
from llm.check_resume_legitimacy import check_resume_legitimacy
from llm.jd_cv_scoring import jd_cv_score
from llm.extract_candidate_info import extract_candidate_info
import hashlib
import re

def extract_email(sender_field):
    match = re.search(r'<(.+?)>', sender_field)
    if match:
        return match.group(1)
    else:
        return sender_field.strip()

def mask_email(email):
    return hashlib.sha256(email.encode()).hexdigest()

if __name__ == "__main__":
    service = get_gmail_service()
    emails = fetch_unread_emails(service)  # returns dict: {sender_email: resume_text}

    for sender_email, resume_text in emails.items():
        clean_email = extract_email(sender_email)
        masked_email = mask_email(clean_email)

        # First, check resume legitimacy
        is_legit = check_resume_legitimacy(resume_text)

        if not is_legit:
            print(f"Rejected {masked_email}: Not a legitimate resume.\n")
            continue  # skip to next email

        jd_cv_matching_score = jd_cv_score(resume_text)
        candidate_info = extract_candidate_info(resume_text)

        print(f"JD-CV Matching Score: {jd_cv_matching_score}%")
        print(f"Candidate Info: {candidate_info}\n")

        if email_exists(masked_email):
            print(f"Email from {masked_email} already exists. Updating record...")
        else:
            print(f"New email from {masked_email}. Inserting into database...")

        save_email_to_db(masked_email, sender_email, jd_cv_matching_score, candidate_info)

        # Send feedback email
        feedback_body = f"""\
Hello,

Thank you for submitting your resume.

Here is your evaluation:

{candidate_info}

JD-CV Matching Score: {jd_cv_matching_score}%

Best Regards,
CV Agent Bot 🤖
"""
        send_email(service, clean_email, "Your Resume Evaluation Report", feedback_body)
