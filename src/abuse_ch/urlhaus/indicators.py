import requests
from src.abuse_ch.config import URLHAUS_BASE_URL, HEADERS
from .normalize import normalize_urlhaus_item

from datetime import datetime, timedelta

def fetch_recent():
    """
    Fetch recent URLhaus IOCs (max 1000) and return only yesterday's IOCs.
    """
    url = f"{URLHAUS_BASE_URL}/urls/recent"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if data.get("query_status") != "ok":
            print(f"[!] Query failed: {data.get('query_status')}")
            return []

        # Filter for yesterday
        yesterday = datetime.utcnow() - timedelta(days=1)
        iocs = []
        for item in data.get("urls", []):
            normalized = normalize_urlhaus_item(item)
            date_added = datetime.strptime(normalized["date_added"], "%Y-%m-%d %H:%M:%S UTC")
            if date_added.date() == yesterday.date():
                iocs.append(normalized)

        print(f"[*] Retrieved {len(iocs)} URLhaus IOCs from yesterday.")
        return iocs

    except requests.exceptions.HTTPError as e:
        print(f"[!] HTTP Error: {e}")
    except Exception as e:
        print(f"[!] Error: {e}")
