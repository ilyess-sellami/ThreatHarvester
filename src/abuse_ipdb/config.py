import os
from dotenv import load_dotenv
from src.config import get_output_file

load_dotenv()

PLATFORM = "abuse_ipdb"

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
BASE_URL = "https://api.abuseipdb.com/api/v2/blacklist"

MAX_LIMIT = 10000
SAFE_SLEEP = 0.5

OUTPUT_FILE = get_output_file(PLATFORM)