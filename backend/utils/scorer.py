from matcher import keyword_match, fuzzy_match

def calculate_score(resume_text, jd_text):
    keyword_score = keyword_match(resume_text, jd_text)
    fuzzy_score = fuzzy_match(resume_text, jd_text)
    final_score = (0.6 * keyword_score) + (0.4 * fuzzy_score)
    return {
        "keyword_score": keyword_score,
        "fuzzy_score": fuzzy_score,
        "final_score": final_score
    }
