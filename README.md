# 📄 CV-Agent: Automating Resume Screening with LLMs + Gmail Integration

Welcome to **CV-Agent**, an intelligent system designed to automate the collection, verification, evaluation, and communication with job applicants — using the power of **Gmail API**, **OpenAI/LLMs**, and **SQLite**!

---

## 🚀 Features

- 🔎 **Fetch Unread Emails**: Automatically retrieves unread emails containing resumes from a Gmail account.
- 🧹 **Resume Legitimacy Check**: Uses LLMs to detect whether a received document is a valid resume.
- 🎯 **JD-CV Matching Score**: Compares the resume against a pre-defined **Job Description** to calculate a **matching score**.
- 🧠 **Candidate Information Extraction**: Extracts:
  - Full Name
  - Work Experience Summary
  - Education Summary
  - Key Skills
  - Relevant Keywords
- 🛡️ **Email Privacy Protection**: Masks candidate email addresses using **SHA-256 hashing** before storing them.
- 🗃️ **Database Integration**: Saves applicant information in a local **SQLite database** with:
  - Masked Email
  - Original Email
  - JD-CV Matching Score
  - Extracted Candidate Info
- 📩 **Automatic Reply to Candidates**: Sends a personalized email back to each applicant with a summary of their extracted details.

---

## 📚 Tech Stack

- **Python 3.10+**
- **Gmail API** (OAuth 2.0 Authentication)
- **OpenRouter/OpenAI API** (for LLM-powered evaluations)
- **SQLite** (Database)
- **dotenv** (Environment Variables Management)

---

## 🛠 Project Structure

```bash
CV-agent/
│
├── gmail_integration/
│   ├── auth.py              # Authenticate with Gmail API
│   ├── fetch_emails.py       # Fetch unread emails
│   └── send_email.py         # Send replies to candidates
│
├── db/
│   ├── db.py                 # SQLite Database setup
│   └── actions.py            # Save and retrieve from DB
│
├── llm/
│   ├── check_resume_legitimacy.py   # Check if a document is a valid resume
│   ├── jd_cv_scoring.py              # Score resume vs job description
│   └── extract_candidate_info.py    # Extract key candidate details
│
├── .env                    # API keys and secrets
├── main.py                 # Main orchestration file
└── README.md               # You are here! 📖

