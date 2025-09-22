import os
import json
from datetime import datetime
from .config import es, helpers, ES_INDEX
from src.config import OUTPUT_DIR


def send_IOCs_to_elasticsearch():
    """
    Read JSON files from outputs/, send IOCs to a single index in Elasticsearch,
    add a timestamp for ingestion, and remove the file after successful insertion.
    """
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(OUTPUT_DIR, filename)
            print(f"[*] Processing file: {filename}")

            with open(filepath, "r", encoding="utf-8") as f:
                iocs = json.load(f)

            if not iocs:
                print("[!] No IOCs found in this file. Removing file.")
                os.remove(filepath)
                continue

            # Add ingestion timestamp to each IOC
            now_str = datetime.utcnow().isoformat()
            for ioc in iocs:
                ioc["_ingested_at"] = now_str

            # Ensure the index exists
            if not es.indices.exists(index=ES_INDEX):
                es.indices.create(index=ES_INDEX)
                print(f"[*] Created index: {ES_INDEX}")

            # Prepare bulk actions
            actions = [{"_index": ES_INDEX, "_source": ioc} for ioc in iocs]

            # Bulk insert
            helpers.bulk(es, actions)
            print(
                f"[*] Inserted {len(iocs)} IOCs into Elasticsearch index '{ES_INDEX}'"
            )

            # Remove the file after successful insertion
            os.remove(filepath)
            print(f"[*] Removed file: {filename}")
