# AI-Powered Resume Screening and Ranking System  

## 📌 Project Overview  
This project automates resume screening and ranking based on job descriptions using **Natural Language Processing (NLP)** and **Machine Learning**. It extracts relevant skills and experience from resumes, compares them with job descriptions, and ranks the resumes accordingly.  

## 🚀 Features  
- 📄 Parses resumes from PDFs  
- 🧠 Extracts skills, experience, and qualifications using **NLTK, SpaCy, and Scikit-learn**  
- 📊 Uses **TF-IDF and similarity matching** for ranking  
- ✅ Provides a ranked list of resumes based on relevance to the job description  


## 🛠️ Tech Stack  
- **Frontend:** Streamlit  
- **Backend:** Python  
- **NLP & Machine Learning:** Scikit-learn, NLTK, SpaCy  
  

## 📂 Project Structure  
📦 AI-Powered-Resume-Screening-and-Ranking-System  
┣ 📜 app.py                   # Main application file (Streamlit frontend)  
┣ 📜 preprocess.py             # Preprocessing functions (NLP & data cleaning)  
┣ 📜 ranking.py                # Resume ranking logic using similarity matching  
┣ 📜 resume_parser.py          # Resume parsing functions  
┣ 📜 requirements.txt          # Dependencies for the project  



## 📥 Installation  
To run this project locally, follow these steps:  

## 1️⃣ Clone this repository
git clone https://github.com/yourusername/resume-screening.git

## 2️⃣ Navigate to the project folder
cd resume-screening

## 3️⃣  Install dependencies
pip install -r requirements.txt

## 4️⃣ Run the application
streamlit run app.py



