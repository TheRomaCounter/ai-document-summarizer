# AI Document Summarizer API

A high-performance, asynchronous microservice built with Python to handle fast document uploads and automated, infrastructure-independent text summarization using local NLP algorithms.

## 🛠️ Tech Stack

* **FastAPI** — High-performance asynchronous Web API for uploading text files and managing processing endpoints.
* **Aiofiles & Python-Multipart** — Non-blocking file I/O operations to handle heavy multi-part document chunk streams.
* **Sumy (LSA Engine)** — Local Latent Semantic Analysis mathematical model for extractive text summarization.
* **NLTK & NumPy** — Specialized linguistic and matrix computation libraries for sentence tokenization and analytical data parsing.

## 📐 Architecture Overview

```text
       [ User ]
          │
     POST /upload
          ▼
   ┌──────────────┐
   │   FastAPI    │
   │   Web API    │
   └──────┬───────┘
          │
     Saves file
          ▼
   ┌──────────────┐
   │ Local Storage│◄────────┐
   │  (/storage)  │         │
   └──────────────┘    Reads file
          │                 │
    POST /summarize         │
          ▼                 │
   ┌──────────────┐         │
   │  AI Service  ├─────────┘
   │ (Local LSA)  │
   └──────┬───────┘
          │
   Returns summary
          ▼
   [ JSON Response ]
```

## 📂 Project Structure

```text
doc_summarizer/
├── storage/               # Local directory for binary file uploads
├── venv/                  # Isolated python virtual environment
├── ai_service.py          # Core NLP architecture and LSA layout logic
├── main.py                # FastAPI routes, schemas and lifestyle triggers
└── requirements.txt       # Frozen environment production packages
```

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher installed on your local operating system.

### Installation

1. Clone the repository and navigate to the root directory:
   ```bash
   cd doc_summarizer
   ```

2. Create and activate an isolated python environment:
   ```bash
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Configure active execution policies and install frozen packages:
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   pip install -r requirements.txt
   ```

4. Spin up the local development web server:
   ```bash
   uvicorn main:app --reload
   ```

5. Explore the live interactive API engine interface at: http://127.0.0
