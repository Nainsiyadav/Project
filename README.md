# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer that compares a candidate's Resume with a Job Description (JD) to calculate the matching percentage and identify missing skills. This project helps users understand how well their resume matches a specific job role and provides suggestions for improvement.

---

## 📌 Features

- 📄 Upload Resume PDF
- 📄 Upload Job Description PDF
- 📖 Extract text from PDF files
- 🧠 Extract skills using a predefined master skill list
- 🔍 Compare Resume skills with Job Description skills
- 📊 Calculate Resume Match Score
- ✅ Display Matched Skills
- ❌ Display Missing Skills
- 💡 Suggest Skills to Improve ATS Score
- 🌐 Web Interface using Flask

---

# 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Libraries
- PyPDF2

### Tools
- VS Code
- Git
- GitHub

---

# 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── uploads/
│
├── python/
│   ├── skills.py
│   ├── extractor.py
│   ├── analyzer.py
│   ├── pdf_reader.py
│
├── README.md
└── requirements.txt
```

---

# ⚙️ Project Workflow

```text
Resume PDF
      │
      ▼
PDF Reader
      │
      ▼
Resume Text
      │
      ▼
Skill Extractor
      │
      ▼
Resume Skills
      │
      ▼
Analyzer
      ▲
JD Skills
      ▲
Skill Extractor
      ▲
JD Text
      ▲
PDF Reader
      ▲
Job Description PDF
      │
      ▼
Match Score
Matched Skills
Missing Skills
Suggestions
```

---

# 📖 How It Works

### Step 1
Upload Resume PDF and Job Description PDF.

### Step 2
Extract text from both PDFs using **PyPDF2**.

### Step 3
Extract technical skills using a predefined master skill list.

### Step 4
Compare Resume Skills with Job Description Skills.

### Step 5
Calculate Resume Match Score.

### Step 6
Display:
- Match Score
- Matched Skills
- Missing Skills
- Suggestions

---

# 📊 Example Output

```text
Match Score : 66.67%

Matched Skills
---------------
Python
SQL

Missing Skills
---------------
C++

Suggestions
---------------
Learn C++
```

---

# 🚀 Future Enhancements

- 🤖 AI-based Skill Suggestions
- 📈 ATS Resume Score
- 📄 Resume Improvement Tips
- 📊 Interactive Dashboard
- 🌙 Dark Mode
- 📥 Download Report as PDF
- 📚 Multiple Resume Comparison
- ☁️ Cloud Deployment

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

Move to the project folder

```bash
cd AI-Resume-Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open in browser

```text
http://127.0.0.1:5000
```

---

# 📷 Screenshots

> Add screenshots of:
- Home Page
- Resume Upload Page
- Result Page

---

# 👩‍💻 Author

**Nainsi Yadav**

🎓 B.Sc. Computer Science Student

💻 Aspiring Software Engineer

🌱 Currently Learning Python, Java, Flask & Backend Development

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.


