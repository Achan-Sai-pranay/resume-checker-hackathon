from fuzzywuzzy import fuzz

def keyword_match(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    return len(resume_words & jd_words) / max(1, len(jd_words)) * 100

def fuzzy_match(resume_text, jd_text):
    return fuzz.token_set_ratio(resume_text, jd_text)
