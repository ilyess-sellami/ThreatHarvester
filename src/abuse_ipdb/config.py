import os
from datetime import datetime
from dotenv import load_dotenv

# Load env vars
load_dotenv()

PLATFORM = "abuse_ipdb"

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
BASE_URL = "https://api.abuseipdb.com/api/v2/blacklist"

today_str = datetime.utcnow().strftime("%Y-%m-%d")
OUTPUT_DIR = "outputs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"iocs_{PLATFORM}_{today_str}.json")

MAX_LIMIT = 10000
SAFE_SLEEP = 0.5
