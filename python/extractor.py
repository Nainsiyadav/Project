# Import skills.py 
from skills import MASTER_SKILLS,ALIASES

# Functions
# resume text
def extract_resume_skills(resume_text) : 
    resume_skills = set()

    #  Text clean
    resume_text = resume_text.replace(","," ")
    resume_text = resume_text.replace("."," ")
    resume_text = resume_text.replace(";"," ")
    resume_text = resume_text.replace("("," ")
    resume_text = resume_text.replace(")"," ")
    resume_text = resume_text.replace(":"," ")
    #  Split
    words = resume_text.split()
    #  Compare with Master skills
    
    for word in words:
        if word in ALIASES:
            word = ALIASES[word]
        
        if word in MASTER_SKILLS:
            resume_skills.add(word)

    return resume_skills

# job description

def extract_jd_skills(jd_text) :
    jd_skills = set()

    # text clean
    jd_text = jd_text.replace(","," ")
    jd_text = jd_text.replace(";"," ")
    jd_text = jd_text.replace("."," ")
    jd_text = jd_text.replace("("," ")
    jd_text = jd_text.replace(")"," ")
    jd_text = jd_text.replace(":"," ")

    # split
    words = jd_text.split()

    #  Compare with Master skills
    for  word in words:
        if word in  ALIASES:
            word  =  ALIASES[word]
    
        if word in  MASTER_SKILLS:
            jd_skills.add(word)
        
    return jd_skills








