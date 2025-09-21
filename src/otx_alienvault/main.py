import os
import json
from .session import make_session
from .pulses import fetch_yesterday_pulses
from .indicators import fetch_pulse_indicators
from .normalize import normalize_indicator
from .config import OUTPUT_DIR, OUTPUT_FILE

def fetch_OTX_Alientvalut_IOCs():
    session = make_session()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("[*] Fetching pulses from yesterday...")
    pulses = fetch_yesterday_pulses(session)
    print(f"[*] Found {len(pulses)} pulses.")

    all_iocs = []
    for pulse in pulses:
        print(f"[*] Fetching indicators for pulse: {pulse.get('name')} ({pulse.get('id')})")
        indicators = fetch_pulse_indicators(session, pulse.get("id"))
        for ind in indicators:
            all_iocs.append(normalize_indicator(ind, pulse))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_iocs, f, indent=2, ensure_ascii=False)

    print(f"[*] Saved {len(all_iocs)} IOCs to {OUTPUT_FILE}")

