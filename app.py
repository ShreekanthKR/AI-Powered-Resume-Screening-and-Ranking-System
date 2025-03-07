import streamlit as st
import os
import tempfile
from resume_parser import extract_text_from_pdf
from preprocess import clean_text
from ranking import rank_resumes

st.title("AI-Powered Resume Screening System")

uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)
job_desc = st.text_area("Enter Job Description")

if st.button("Rank Resumes"):
    if uploaded_files and job_desc:
        resume_data = []  # Store tuples of (filename, cleaned_text)
        
        for uploaded_file in uploaded_files:
            filename = uploaded_file.name
            
            # Save the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.read())
                temp_path = temp_file.name
            
            text = extract_text_from_pdf(temp_path)  # Extract text from PDF
            os.remove(temp_path)  # Clean up temp file after extraction
            
            cleaned_text = clean_text(text)
            resume_data.append((filename, cleaned_text))

        filenames, texts = zip(*resume_data)

        # Rank resumes based on similarity
        ranked_indices_scores = rank_resumes(job_desc, texts)  # Returns [(index, score)]

        # Map ranked indices back to filenames
        ranked_results = [(filenames[i], score) for i, score in ranked_indices_scores]

        st.subheader("Top Ranked Resumes:")
        for i, (filename, score) in enumerate(ranked_results):
            st.write(f"**Rank {i+1}: {filename} - Score {score:.2f}**")
    else:
        st.warning("Please upload resumes and enter a job description.")
