from matcher import keyword_match, fuzzy_match

def calculate_scores(resume_text, jd_text):
    """Calculate keyword score, fuzzy score, and final weighted score."""
    keyword_score = keyword_match(resume_text, jd_text)
    fuzzy_score = fuzzy_match(resume_text, jd_text)

    # Weighted formula: 60% keywords, 40% fuzzy
    final_score = round((0.6 * keyword_score) + (0.4 * fuzzy_score), 2)

    return {
        "keyword_score": keyword_score,
        "fuzzy_score": fuzzy_score,
        "final_score": final_score
    }