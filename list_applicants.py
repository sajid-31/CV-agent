# list_applicants.py

from db.db import conn, cursor

def list_applicants():
    cursor.execute('SELECT original_email, created_at FROM applicants ORDER BY created_at DESC')
    applicants = cursor.fetchall()

    if not applicants:
        print("❌ No applicants found.")
    else:
        print(f"\n📋 List of Applicants ({len(applicants)} total):\n")
        for idx, (email, timestamp) in enumerate(applicants, 1):
            print(f"{idx}. 📧 Email: {email}\n   🕒 Submitted At: {timestamp}\n")

if __name__ == "__main__":
    list_applicants()
