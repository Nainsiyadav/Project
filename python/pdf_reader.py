import PyPDF2
def extract_resume_text(pdf_path):
    pdf_file = open(pdf_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    pdf_file.close()
    return text

def extract_jd_text(pdf_path):
    pdf_file = open(pdf_path,"rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    pdf_file.close()
    return text

