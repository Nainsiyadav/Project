# import all files
from pdf_reader import extract_resume_text, extract_jd_text
from extractor import extract_resume_skills , extract_jd_skills
from analyzer import analyze_resume
# give path of resume and jd files
resume_path = "Project/python/resume.pdf"
jd_path = "Project/python/jd.pdf"

resume_text = extract_resume_text(resume_path)
jd_text = extract_jd_text(jd_path)

resume_skill = extract_resume_skills(resume_text)
jd_skill = extract_jd_skills(jd_text)

matched_skill, missing_skill, match_score, suggetion = analyze_resume(resume_skill,jd_skill)

print("matched_skill : ",matched_skill)
print("match_score : ",match_score)
print("missing_skill : ",missing_skill)
print("Suggetion : ",suggetion)