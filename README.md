# AI Document Summarizer API

A fast, lightweight, and completely autonomous REST API built with FastAPI that uses Natural Language Processing (NLP) to generate automatic summaries of text documents.

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **Deployment/Server:** Uvicorn
* **NLP & Text Analytics:** Sumy (LSA Framework) & NLTK
* **Data Processing:** NumPy

## 🚀 Key Features
* **File Upload Management:** Securely uploads `.txt` documents to local server storage using asynchronous chunks via `aiofiles`.
* **100% Offline AI Summarization:** Uses a local Latent Semantic Analysis (LSA) mathematical algorithm to extract key sentences without relying on external APIs, subscription keys, or internet connectivity.
* **Auto-Dependency Resolution:** Dynamically verifies, updates, and downloads required language structures and library assets on startup.

## 💻 How to Run
1. Clone the repository.
2. Install all core assets:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
4. Access interactive endpoint UI at: http://127.0.0
