def normalize(entry, fetched_at):
    return {
        "source": "AbuseIPDB",
        "indicator": entry.get("ipAddress"),
        "type": (
            "ipv4" if entry.get("ipAddress") and "." in entry.get("ipAddress") else "ip"
        ),
        "abuse_confidence_score": entry.get("abuseConfidenceScore"),
        "last_reported_at": entry.get("lastReportedAt"),
        "country": entry.get("countryCode"),
        "total_reports": entry.get("totalReports"),
        "fetched_at": fetched_at,
    }
