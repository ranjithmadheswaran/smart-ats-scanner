# 📄 Smart ATS Resume Scanner

A Streamlit web application that leverages the power of Google's Gemini AI to function as a smart Applicant Tracking System (ATS). This tool helps job seekers analyze their resumes against a job description, providing a percentage match, identifying missing keywords, and offering actionable suggestions for improvement.

 <!-- It's a good idea to add a screenshot of your app here! -->

---

## ✨ Features

- **AI-Powered Analysis**: Uses the Gemini AI API for intelligent resume and job description parsing.
- **Job Description Match**: Calculates a percentage score indicating how well the resume matches the job description.
- **Missing Keyword Detection**: Identifies crucial keywords from the job description that are missing in the resume.
- **AI Profile Summary**: Generates a concise summary of the candidate's profile based on the provided documents.
- **Actionable Suggestions**: Provides concrete advice on how and where to incorporate missing keywords into the resume.
- **Simple Web Interface**: Built with Streamlit for a clean and user-friendly experience.
- **PDF Parsing**: Directly extracts text from uploaded PDF resumes.

---

## 🛠️ Setup & Installation

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/ranjithmadheswaran/smart-ats-scanner.git
cd smart-ats-scanner
```

### 2. Create a Virtual Environment (Recommended)

```bash
# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Get Your Google AI API Key

You need an API key to use the Gemini model. You can get one for free from Google AI Studio.

---

## 🚀 How to Run the Application

1.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run hello.py
    ```
2.  Your web browser will open a new tab with the application.
3.  Enter your Google AI API Key.
4.  Paste the job description into the text area.
5.  Upload your resume in PDF format.
6.  Click the **"Analyze My Resume"** button and wait for the report!