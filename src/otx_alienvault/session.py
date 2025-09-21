import requests
from .config import API_KEY


def make_session():
    if not API_KEY:
        raise SystemExit("[!] Set OTX_API_KEY in .env file")
    session = requests.Session()
    session.headers.update(
        {
            "X-OTX-API-KEY": API_KEY,
            "User-Agent": "OTX-Yesterday-IOCs/1.0",
            "Accept": "application/json",
        }
    )
    return session


def request_fast(session, url, params=None):
    r = session.get(url, params=params)
    r.raise_for_status()
    return r.json()
