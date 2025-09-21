import time
import requests
from .config import API_KEY, BASE_URL, MAX_LIMIT, SAFE_SLEEP


def make_session():
    if not API_KEY:
        raise SystemExit("[!] ABUSEIPDB_API_KEY missing in .env")
    s = requests.Session()
    s.headers.update({"Accept": "application/json", "Key": API_KEY})
    return s


def fetch_blacklist(limit=MAX_LIMIT):
    params = {"limit": limit}
    session = make_session()
    r = session.get(BASE_URL, params=params, timeout=60)
    r.raise_for_status()
    time.sleep(SAFE_SLEEP)
    return r.json().get("data", [])