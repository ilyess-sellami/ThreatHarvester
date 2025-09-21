from .session import request_fast
from .config import BASE_URL, PAGE_SIZE_INDICATORS


def fetch_pulse_indicators(session, pulse_id):
    url = f"{BASE_URL}/pulses/{pulse_id}/indicators"
    params = {"page": 1, "limit": PAGE_SIZE_INDICATORS}
    indicators = []

    while url:
        data = request_fast(session, url, params=params)
        results = data.get("results") or data.get("indicators") or []
        indicators.extend(results)
        url = data.get("next")
        params = None

    return indicators
