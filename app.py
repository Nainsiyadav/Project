from flask import Flask, render_template, request
import os
from python.pdf_reader import extract_resume_text, extract_jd_text
from python.extractor import extract_resume_skills, extract_jd_skills
from python.analyzer import analyze_resume
from python.skills import MASTER_SKILLS, ALIASES

app = Flask(__name__)
UPLOAD_FOLDER = "Uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    jd = request.files["jd"]

    resume_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )
    jd_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        jd.filename
    )

    resume.save(resume_path)
    jd.save(jd_path)

    resume_text = extract_resume_text(resume_path)
    jd_text = extract_jd_text(jd_path)

    resume_skills = extract_resume_skills(resume_text)
    jd_skills = extract_jd_skills(jd_text)

    matched_skill, missing_skill, match_score, suggestion = analyze_resume(resume_skills,jd_skills)

    print("Resume Text:")
    print(resume_text)

    print("Jd Text")
    print(jd_text)

    print("Resume : ",resume.filename)
    print("jd : ",jd.filename)

    return render_template(
        "result.html",
        matched_skill=matched_skill,
        missing_skill=missing_skill,
        match_score=match_score,
        suggestion=suggestion
    )

if __name__ == "__main__":
    app.run(debug=True)