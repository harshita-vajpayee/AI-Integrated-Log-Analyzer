from fastapi import APIRouter, UploadFile, File
import os
from app.utils.log_parser import parse_log_file
from app.services.gemini_service import analyze_log_with_ai

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # ensures the folder exists

@router.post("/analyze")
async def analyze_log(logFile: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, logFile.filename)

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            buffer.write(await logFile.read())

        # Parse the log
        log_data = parse_log_file(file_path)

        # AI analysis
        ai_result = analyze_log_with_ai(log_data)

        # Clean up file
        os.remove(file_path)

        return {
            "success": True,
            "analysis": ai_result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
