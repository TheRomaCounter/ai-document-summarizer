import os
import aiofiles
from fastapi import FastAPI, UploadFile, File, HTTPException
import ai_service

app = FastAPI(title="AI Document Summarizer API")

STORAGE_DIR = "storage"

if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")
        
    file_path = os.path.join(STORAGE_DIR, file.filename)
    
    async with aiofiles.open(file_path, "wb") as buffer:
        content = await file.read()
        await buffer.write(content)
        
    return {
        "status": "success",
        "filename": file.filename,
        "message": "File uploaded successfully."
    }

@app.post("/summarize")
async def summarize_file(filename: str):
    file_path = os.path.join(STORAGE_DIR, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found in storage.")
        
    async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
        text_content = await f.read()
        
    if not text_content.strip():
        raise HTTPException(status_code=400, detail="File is empty.")
        
    summary = ai_service.summarize_text(text_content)
    
    return {
        "filename": filename,
        "summary": summary
    }
