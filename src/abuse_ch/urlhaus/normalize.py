
def normalize_urlhaus_item(item):
    """
    Normalize a single URLhaus entry to a standard IOC dict.
    """
    return {
        "source": "URLhaus - abuse.ch",
        "type": "url",
        "indicator": item.get("url"),
        "host": item.get("host"),
        "date_added": item.get("date_added"),
        "threat": item.get("threat"),
        "blacklists": item.get("blacklists"),
        "reporter": item.get("reporter"),
        "tags": item.get("tags"),
        "payloads": item.get("payloads")
    }
