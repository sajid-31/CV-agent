def jd_cv_score(resume_text):
    with open('job_description.txt', 'r') as f:
        job_description = f.read()

    jd_keywords = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())

    matching_keywords = jd_keywords.intersection(resume_words)
    score = (len(matching_keywords) / len(jd_keywords)) * 100

    return round(score, 2)
