def normalize_indicator(ind, pulse):
    return {
        "source": "OTX",
        "indicator": ind.get("indicator") or ind.get("value"),
        "type": ind.get("type") or ind.get("indicator_type"),
        "pulse_id": pulse.get("id"),
        "pulse_name": pulse.get("name"),
        "created": ind.get("created") or pulse.get("created"),
        "modified": ind.get("modified") or pulse.get("modified"),
        "tags": pulse.get("tags", []),
        "tlp": pulse.get("tlp"),
    }
