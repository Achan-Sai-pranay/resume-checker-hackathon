import re
from collections import Counter
from fuzzywuzzy import fuzz

def clean_text(text):
    """Lowercase and remove special characters."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text

def keyword_match(resume_text, jd_text):
    """Count keyword overlap between resume and job description."""
    resume_words = clean_text(resume_text).split()
    jd_words = clean_text(jd_text).split()

    resume_counts = Counter(resume_words)
    jd_counts = Counter(jd_words)

    common = set(resume_counts.keys()) & set(jd_counts.keys())
    if not jd_counts:
        return 0.0
    score = (len(common) / len(set(jd_counts.keys()))) * 100
    return round(score, 2)

def fuzzy_match(resume_text, jd_text):
    """Fuzzy string similarity between resume and JD."""
    score = fuzz.token_set_ratio(resume_text, jd_text)
    return round(score, 2)