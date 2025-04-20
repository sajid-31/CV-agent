import sqlite3
import os

# Ensure the db folder exists
os.makedirs('db', exist_ok=True)

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('db/applicants.db', check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS applicants (
    masked_email TEXT PRIMARY KEY,
    original_email TEXT,
    jd_cv_score REAL,
    candidate_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()
