import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OTX_API_KEY")
PLATFORM = "otx"

# Output folder outside /src
OUTPUT_DIR = os.path.abspath("outputs")
today_str = datetime.utcnow().strftime("%Y-%m-%d")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"iocs_{PLATFORM}_{today_str}.json")

BASE_URL = "https://otx.alienvault.com/api/v1"
PAGE_SIZE_PULSES = 50
PAGE_SIZE_INDICATORS = 100
