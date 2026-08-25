from flask import Flask, render_template, request, session, send_file
import os
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from python.pdf_reader import extract_resume_text, extract_jd_text
from python.extractor import extract_resume_skills, extract_jd_skills
from python.analyzer import analyze_resume

app = Flask(__name__)

app.secret_key = "resume_analyzer_secret"

UPLOAD_FOLDER = "Uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# ANALYZE RESUME
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

    # Save uploaded files
    resume.save(resume_path)
    jd.save(jd_path)

    # Extract text from PDFs
    resume_text = extract_resume_text(resume_path)
    jd_text = extract_jd_text(jd_path)

    # Extract skills
    resume_skills = extract_resume_skills(resume_text)
    jd_skills = extract_jd_skills(jd_text)

    # Analyze skills
    matched_skill, missing_skill, match_score, suggestion = analyze_resume(
        resume_skills,
        jd_skills
    )

    # Save data in session
    session["matched_skill"] = list(matched_skill)
    session["missing_skill"] = list(missing_skill)
    session["match_score"] = match_score
    session["suggestion"] = list(suggestion)

    # Show result page
    return render_template(
        "result.html",
        matched_skill=matched_skill,
        missing_skill=missing_skill,
        match_score=match_score,
        suggestion=suggestion
    )


# DOWNLOAD PDF REPORT
@app.route("/download-report")
def download_report():

    matched_skill = session.get("matched_skill", [])
    missing_skill = session.get("missing_skill", [])
    match_score = session.get("match_score", 0)
    suggestion = session.get("suggestion", [])

    # Create PDF in memory
    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(150, 750, "AI Resume Analysis Report")

    # Match Score
    c.setFont("Helvetica", 14)
    c.drawString(
        100,
        700,
        f"Match Score: {match_score}%"
    )

    # Matched Skills
    c.drawString(
        100,
        650,
        "Matched Skills: " + ", ".join(matched_skill)
    )

    # Missing Skills
    c.drawString(
        100,
        600,
        "Missing Skills: " + ", ".join(missing_skill)
    )

    # Suggestions
    c.drawString(
        100,
        550,
        "Suggestions: " + ", ".join(suggestion)
    )

    # Save PDF
    c.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="AI_Resume_Report.pdf",
        mimetype="application/pdf"
    )


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)