import os
from dotenv import load_dotenv
from src.config import get_output_file

load_dotenv()

API_KEY = os.getenv("ABUSE_CH_API_KEY")
PLATFORM="abuse_ch"

if not API_KEY:
    raise ValueError("Please set ABUSE_CH_API_KEY in your .env file")

HEADERS = {"Auth-Key": API_KEY}
URLHAUS_BASE_URL = "https://urlhaus-api.abuse.ch/v1"
MALWAREBAZAAR_BASE_URL = "https://mb-api.abuse.ch/api/v1"


URLHAUS_OUTPUT_FILE = get_output_file(PLATFORM, "urlhaus")
MALWAREBAZAAR_OUTPUT_FILE = get_output_file(PLATFORM, "malwarebazaar")
