# 💼 AI Job Recommender System (Real-Time + Semantic Matching)

An intelligent job recommendation system that scrapes live job postings and delivers personalized job matches using **semantic similarity powered by transformer models**.

---

## 🚀 Overview

This project helps job seekers discover relevant opportunities by combining:

* 📡 Real-time job scraping
* 📄 Resume analysis
* 🧠 Transformer-based NLP matching

Unlike traditional systems that rely on keyword matching, this system understands **context and meaning**, providing more accurate recommendations.

---

## ✨ Key Features

### 🔍 Real-Time Job Scraping

* Dynamically fetches job listings from an online source (RemoteOK)
* Ensures up-to-date job recommendations

### 📄 Resume Parsing

* Extracts skills and relevant information from uploaded resumes
* Supports structured and unstructured formats

### 🧠 Semantic Recommendation Engine

* Uses **Sentence Transformers** to generate embeddings
* Computes **Cosine Similarity** to rank job relevance

### 🎯 Flexible Input System

* Upload resume OR input skills manually
* Combines both for improved accuracy

### ⚡ On-Demand Processing

* Recommendations are generated only when triggered
* Efficient and scalable design

---

## 🏗️ System Workflow

```text
User Input / Resume
        ↓
Resume Parsing (NLP)
        ↓
Skill Extraction
        ↓
Job Scraper (Live Data)
        ↓
Text Embedding (Sentence Transformers)
        ↓
Similarity Matching (Cosine Similarity)
        ↓
Top Job Recommendations
```

---

## 🛠️ Tech Stack

* **Python 3.11**
* **Streamlit** – Interactive UI
* **Pandas / NumPy** – Data processing
* **Sentence Transformers** – Semantic embeddings
* **Scikit-learn** – Cosine similarity
* **Requests** – Web scraping

---

## 📂 Project Structure

```bash
Job_Recommender/
│
├── app.py                    # Streamlit app entry point
├── job_scraper.py            # Job scraping logic
├── recommender.py            # Recommendation engine
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/Codaks-py/Job_Recommender.git

# Navigate into project
cd Job_Recommender

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

### Steps:

1. Upload your resume OR enter skills manually
2. Click **"Get Recommendations"**
3. View ranked job matches instantly

---

## 📊 Output

The system returns:

* 💼 Job Title
* 🏢 Company
* 📈 Match Score (%)
* 🧠 Relevant Skills
* 🔗 Job Link

---

## 🧠 How the Recommendation Works

This system uses **semantic similarity powered by transformer models**:

* Text from resumes and job descriptions is encoded using **Sentence Transformers**
* Each input is converted into a dense vector (embedding)
* **Cosine similarity** is used to measure closeness
* Jobs are ranked based on semantic relevance

### ✅ Why This Approach?

* Understands **context, not just keywords**
* Matches similar meanings:

  * *"ML Engineer"* ≈ *"Machine Learning Developer"*
* Significantly more accurate than traditional methods

---

## 🧠 Key ML Highlight

This project demonstrates a **real-world NLP application** using:

* Transformer-based embeddings
* Semantic search / retrieval systems
* End-to-end ML pipeline integration

Similar techniques are used in modern platforms like LinkedIn and Indeed.

---

## 🔥 Why This Project Stands Out

* Combines **ML + NLP + Data Engineering + UI**
* Uses **real-time job data (not static datasets)**
* Implements **transformer-based recommendation system**
* Built as an **end-to-end deployable application**

---

## 🚀 Future Improvements

* 🌐 Multi-source job scraping (LinkedIn, Indeed APIs)
* 🤖 Upgrade to advanced embeddings (fine-tuned models)
* 🧩 User profiles & saved jobs
* 📊 Analytics dashboard
* 📬 Email job alerts

---

## 🤝 Contributing

Contributions are welcome!

```bash
git checkout -b feature-name
git commit -m "Add feature"
git push origin feature-name
```

---
