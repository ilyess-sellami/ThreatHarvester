import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

ABUSE_CH_API_KEY = os.getenv("ABUSE_CH_API_KEY")
PLATFORM="abuse_ch"

if not ABUSE_CH_API_KEY:
    raise ValueError("Please set ABUSE_CH_API_KEY in your .env file")

HEADERS = {"Auth-Key": ABUSE_CH_API_KEY}
URLHAUS_BASE_URL = "https://urlhaus-api.abuse.ch/v1"


OUTPUT_DIR = "outputs"
today_str = datetime.utcnow().strftime("%Y-%m-%d")
URLHAUS_OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"iocs_{PLATFORM}_urlhaus_{today_str}.json")
