import json
from datetime import datetime
from .normalize import normalize
from .indicators import fetch_blacklist
from .config import MAX_LIMIT, OUTPUT_FILE


def fetch_AbuseIPDB_IOCs():

    print(f"[*] Fetching blacklist entries from AbuseIPDB (limit {MAX_LIMIT})...")
    entries = fetch_blacklist(MAX_LIMIT)
    print(f"[*] Retrieved {len(entries)} entries")

    fetched_at = datetime.utcnow().isoformat() + "Z"
    normalized = [normalize(e, fetched_at) for e in entries]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(normalized, f, indent=2, ensure_ascii=False)

    print(f"[*] Saved {len(normalized)} IOCs → {OUTPUT_FILE}")
    return OUTPUT_FILE
