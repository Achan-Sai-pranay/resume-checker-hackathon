from fastapi import FastAPI, UploadFile, Form
import os
from parser import parse_resume, parse_job_description
from scorer import calculate_score
from feedback import generate_feedback
from config import UPLOAD_DIR

app = FastAPI()

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.post("/match/")
async def match_resume(resume: UploadFile, jd_text: str = Form(...)):
    # save file
    file_path = os.path.join(UPLOAD_DIR, resume.filename)
    with open(file_path, "wb") as f:
        f.write(await resume.read())

    # parse & score
    resume_text = parse_resume(file_path)
    jd_parsed = parse_job_description(jd_text)
    scores = calculate_score(resume_text, jd_parsed)
    feedback = generate_feedback(scores)

    return {"scores": scores, "feedback": feedback}
