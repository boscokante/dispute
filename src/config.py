import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GPT_MODEL = "gpt-4"

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")