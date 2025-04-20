from db.db import conn, cursor

def save_email_to_db(masked_email, original_email, jd_cv_score, candidate_info):
    cursor.execute('''
    INSERT INTO applicants (masked_email, original_email, jd_cv_score, candidate_info)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(masked_email) DO UPDATE SET
        original_email=excluded.original_email,
        jd_cv_score=excluded.jd_cv_score,
        candidate_info=excluded.candidate_info,
        created_at=CURRENT_TIMESTAMP
    ''', (masked_email, original_email, jd_cv_score, candidate_info))
    conn.commit()
    print('✅ Email saved/updated in database.')

def email_exists(masked_email):
    cursor.execute('SELECT 1 FROM applicants WHERE masked_email = ?', (masked_email,))
    return cursor.fetchone() is not None
