def generate_feedback(score_dict):
    feedback = []
    if score_dict["keyword_score"] < 50:
        feedback.append("Resume is missing many required keywords from JD.")
    else:
        feedback.append("Resume covers most keywords in JD.")

    if score_dict["fuzzy_score"] < 60:
        feedback.append("Improve phrasing/terminology to match job description.")
    else:
        feedback.append("Resume language matches job description fairly well.")

    if score_dict["final_score"] > 75:
        feedback.append("Overall: Strong fit ✅")
    elif score_dict["final_score"] > 50:
        feedback.append("Overall: Moderate fit ⚠️")
    else:
        feedback.append("Overall: Weak fit ❌")

    return feedback
