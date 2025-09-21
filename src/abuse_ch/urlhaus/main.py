import os
import json
from .indicators import fetch_recent
from src.abuse_ch.config import OUTPUT_DIR, URLHAUS_OUTPUT_FILE


def fetch_AbuseCH_URLhaus_IOCs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("[*] Fetching recent URLhaus URLs...")
    normalized_iocs = fetch_recent()

    with open(URLHAUS_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(normalized_iocs, f, indent=2, ensure_ascii=False)

    print(f"[*] Saved {len(normalized_iocs)} IOCs to {URLHAUS_OUTPUT_FILE}")
