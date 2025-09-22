import os
from dotenv import load_dotenv
from src.config import get_output_file

load_dotenv()

API_KEY = os.getenv("OTX_API_KEY")
PLATFORM = "otx"

BASE_URL = "https://otx.alienvault.com/api/v1"
PAGE_SIZE_PULSES = 50
PAGE_SIZE_INDICATORS = 100


OUTPUT_FILE = get_output_file(PLATFORM)