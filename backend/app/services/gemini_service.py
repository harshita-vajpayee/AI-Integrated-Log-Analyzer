import os
from dotenv import load_dotenv
import google.generativeai as genai  # correct import

load_dotenv()  # load .env

# Configure API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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
    response = genai.chat.create(
        model="models/text-bison-001",
        messages=[{"author": "user", "content": prompt}]
    )
    return response.last
