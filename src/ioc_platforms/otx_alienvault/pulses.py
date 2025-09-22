from datetime import datetime, timedelta
from .session import request_fast
from .config import BASE_URL, PAGE_SIZE_PULSES


def parse_datetime(dt_str):
    if not dt_str:
        return None
    dt_str = dt_str.rstrip("Z")
    return datetime.fromisoformat(dt_str)


def fetch_yesterday_pulses(session):
    yesterday = (datetime.utcnow() - timedelta(days=1)).date()
    url = f"{BASE_URL}/pulses/subscribed"
    params = {"page": 1, "limit": PAGE_SIZE_PULSES}
    yesterday_pulses = []

    stop_loop = False
    while url and not stop_loop:
        data = request_fast(session, url, params=params)
        stop_loop = True

        for pulse in data.get("results", []):
            created_dt = parse_datetime(pulse.get("created"))
            modified_dt = parse_datetime(pulse.get("modified"))

            if (created_dt and created_dt.date() == yesterday) or (
                modified_dt and modified_dt.date() == yesterday
            ):
                yesterday_pulses.append(pulse)
                stop_loop = False

        url = data.get("next")
        params = None

    return yesterday_pulses
