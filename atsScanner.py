import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import json
import re

def get_gemini_response(input_prompt):
    """
    Calls the Gemini model to get a response based on the input prompt.
    """
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content(input_prompt)
    return response.text

def input_pdf_text(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    """
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# The prompt template for the Gemini API call
input_prompt_template = """
You are an experienced Applicant Tracking System (ATS) and a professional career coach with a deep understanding of the tech industry, including software engineering, data science, and data analysis. Your task is to evaluate a resume against a given job description and provide actionable feedback.

**Instructions:**
1.  **Job Description Match:** Calculate a percentage match between the resume and the job description. This should be a string like "85%".
2.  **Missing Keywords:** Identify and list critical keywords from the job description that are absent in the resume. This should be a list of strings.
3.  **Profile Summary:** Provide a brief summary of the candidate's profile, highlighting strengths and areas for improvement based on the job description.
4.  **Improvement Suggestions:** For the "Missing Keywords" you identified, provide specific, actionable suggestions on how the candidate can incorporate them into their resume. For each suggestion, explain where it might fit (e.g., in a project description, skills section, or summary) and provide an example sentence. This should be a well-structured string or markdown text.

Please provide the output as a single JSON object with the following keys: "JD Match", "MissingKeywords", "Profile Summary", and "ImprovementSuggestions".

**Resume:**
{resume_text}

**Job Description:**
{jd}
"""

# --- Streamlit App ---
st.set_page_config(page_title="Smart ATS", page_icon=":robot_face:")
st.title("📄 Smart ATS Resume Scanner")
st.markdown("##### Analyze your resume against any job description to improve your chances!")

api_key = st.text_input("Enter your Google AI API Key:", type="password", help="Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).")

jd = st.text_area("Paste the Job Description here:", height=250)
uploaded_file = st.file_uploader("Upload Your Resume (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume Uploaded Successfully!")

submit_button = st.button("Analyze My Resume")

if submit_button:
    if api_key and jd and uploaded_file:
        with st.spinner("Analyzing your resume... This might take a moment."):
            try:
                genai.configure(api_key=api_key)
                resume_text = input_pdf_text(uploaded_file)
                full_prompt = input_prompt_template.format(resume_text=resume_text, jd=jd)

                response_text = get_gemini_response(full_prompt)

                # Clean the response to ensure it's valid JSON
                # Gemini can sometimes return the JSON wrapped in ```json ... ```
                match = re.search(r'```json\s*(\{.*?\})\s*```', response_text, re.DOTALL)
                json_str = match.group(1) if match else response_text

                response_json = json.loads(json_str)

                st.subheader("📊 Analysis Report")

                # Display Percentage Match with a progress bar
                match_percentage = int(re.search(r'\d+', response_json.get("JD Match", "0%")).group())
                st.markdown(f"### **Job Description Match: {match_percentage}%**")
                st.progress(match_percentage)

                st.markdown("### **Profile Summary**")
                st.write(response_json.get("Profile Summary", "No summary provided."))

                st.markdown("### **Missing Keywords**")
                missing_keywords = response_json.get("MissingKeywords", [])
                if missing_keywords:
                    st.warning("Consider adding these keywords to your resume: " + ", ".join(missing_keywords))
                else:
                    st.success("🎉 Your resume seems to cover all the important keywords!")

                st.markdown("### **💡 Resume Improvement Suggestions**")
                suggestions = response_json.get("ImprovementSuggestions")
                if suggestions:
                    st.info(suggestions)
                else:
                    st.write("No specific improvement suggestions were generated.")

            except (json.JSONDecodeError, AttributeError):
                st.error("❌ Error: Failed to parse the AI's response. The format might be unexpected.")
                st.write("Here is the raw response from the AI:")
                st.code(response_text)
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("⚠️ Please provide the API Key, Job Description, and upload your Resume to proceed.")