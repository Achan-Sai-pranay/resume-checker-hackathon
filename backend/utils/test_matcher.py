from parser import parse_resume
from scorer import calculate_scores

# Load resume text (using your existing sample PDF)
resume_file = "sample_resumes/functionalsample.pdf"
resume_text = parse_resume(resume_file)

# Example Job Description
jd_text = """
We are hiring a Software Engineer skilled in Python, SQL, and Machine Learning.
Responsibilities include data analysis, building AI models, and API development.
"""

# Run scoring
scores = calculate_scores(resume_text, jd_text)

print("📊 Matching Scores:")
print(scores)