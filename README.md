# AI Document Summarizer API

A modern, high-performance asynchronous REST API built with FastAPI that processes and generates automated text summaries from document files.

## Tech Stack
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Asynchronous I/O:** `aiofiles`
* **File Handling:** `python-multipart`
* **NLP & Analytics:** `sumy` (LSA Engine), `nltk`
* **Math Matrix Operations:** `numpy`

## Features
* **File Pipelines:** Supports asynchronous multi-part document chunk streams to bypass main loop blocking.
* **Autonomous Execution:** Relies entirely on local Latent Semantic Analysis (LSA) vectors. It operates without external cloud dependencies, proxy keys, or active network layers.
* **Auto-Patch Mechanics:** Implements dynamic startup triggers to evaluate, install, and resolve environment dependencies at execution time.
