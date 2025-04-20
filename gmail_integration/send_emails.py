import base64
from email.mime.text import MIMEText

def send_email(service, to_email, subject, body):
    message = MIMEText(body)
    message['to'] = to_email
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    send_message = service.users().messages().send(
        userId="me",
        body={'raw': raw_message}
    ).execute()

    print(f"📧 Email sent to {to_email}")
