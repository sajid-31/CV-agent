import base64
from googleapiclient.errors import HttpError

def fetch_unread_emails(service):
    results = {}
    try:
        response = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
        messages = response.get('messages', [])

        print(f"Found {len(messages)} unread emails.")

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            payload = msg['payload']
            headers = payload['headers']
            sender = next((header['value'] for header in headers if header['name'] == 'From'), None)

            parts = payload.get('parts', [])
            resume_text = ""

            for part in parts:
                if part['mimeType'] == 'text/plain':
                    resume_text = base64.urlsafe_b64decode(part['body']['data']).decode()

            if sender and resume_text:
                results[sender] = resume_text

            # Mark the message as read
            service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()

    except HttpError as error:
        print(f'An error occurred: {error}')
    
    return results
