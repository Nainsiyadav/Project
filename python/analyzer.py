
def  analyze_resume(resume_skills,jd_skills):
    # Matched Skills
    matched_skills = resume_skills & jd_skills
    # Missing Skills
    missing_skills =  jd_skills - resume_skills
    # Matched  Score
    if len(jd_skills) > 0 :
       match_score = round((len(matched_skills)/len(jd_skills))*100,2)
    else:
        match_score = 0
    # Suggestion
    suggestion = missing_skills

    return matched_skills,missing_skills,match_score,suggestion