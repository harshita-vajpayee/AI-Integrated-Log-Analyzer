# app/services/gemini_service.py
import os
from dotenv import load_dotenv
from google import genai  # new package

load_dotenv()  # loads .env

# Get API key
API_KEY = "AIzaSyADbRFBBQzO1aLzQTxqQscSbcc2TsWpDlw"
#os.getenv("GEMINI_API_KEY")
# Create a client
client = genai.Client(api_key=API_KEY)

def analyze_log_with_ai(log_data: str) -> str:
    prompt = f"""
You are a senior software engineer.

Analyze the following application log and respond STRICTLY in JSON with keys:
- errorType
- severity (Low/Medium/High)
- rootCause
- suggestedFix
- summary

LOG DATA:
{log_data}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # supported model
        contents=prompt
    )
    return response.text