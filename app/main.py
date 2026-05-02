from fastapi import FastAPI, UploadFile, File
import os

from app.core.config import HAR_FILE, GENERATED_FILE
from app.parser.har_parser import load_har, get_entries
from app.parser.extractor import extract_requests
from app.utils.cleaner import clean_requests
from app.generator.api_generator import generate_fastapi_routes

app = FastAPI(title="Browser2API 🚀")


@app.get("/")
def root():
    return {"message": "Browser2API running"}


@app.post("/upload-har/")
async def upload_har(file: UploadFile = File(...)):
    os.makedirs("data", exist_ok=True)

    content = await file.read()
    with open(HAR_FILE, "wb") as f:
        f.write(content)

    return {"status": "HAR uploaded"}


@app.post("/generate/")
def generate():
    har_data = load_har(HAR_FILE)
    entries = get_entries(har_data)

    extracted = extract_requests(entries)
    cleaned = clean_requests(extracted)

    code = generate_fastapi_routes(cleaned)

    os.makedirs("generated", exist_ok=True)

    with open(GENERATED_FILE, "w") as f:
        f.write(code)

    return {
        "status": "generated",
        "endpoints": len(cleaned)
    }


@app.get("/preview/")
def preview():
    if not os.path.exists(GENERATED_FILE):
        return {"error": "Generate API first"}

    with open(GENERATED_FILE, "r") as f:
        return {"code": f.read()}