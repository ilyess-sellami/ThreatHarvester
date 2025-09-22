from fastapi import FastAPI
import schedule
import time
import threading
from src import (
    fetch_OTX_Alientvalut_IOCs,
    fetch_AbuseIPDB_IOCs,
    fetch_AbuseCH_URLhaus_IOCs,
    fetch_AbuseCH_MalwareBazaar_IOCs,
    send_IOCs_to_elasticsearch
)


# ---------------- FastAPI App ----------------
app = FastAPI(title="Threat Harvester")


# ---------------- Scheduler Job ----------------
def job():
    print("[*] Running daily OTX fetch...")
    fetch_OTX_Alientvalut_IOCs()

    print("[*] Running daily AbuseIPDB fetch...")
    fetch_AbuseIPDB_IOCs()
    
    print("[*] Running daily URLhaus fetch...")
    fetch_AbuseCH_URLhaus_IOCs()
    
    print("[*] Running daily MalwareBazaar fetch...")
    fetch_AbuseCH_MalwareBazaar_IOCs()
    
    print("[*] Sending collected IOCs to Elasticsearch...")
    send_IOCs_to_elasticsearch()
    
    

def run_scheduler():
    # Runs daily at 1 AM UTC
    schedule.every().day.at("01:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)


# ---------------- Startup Event ----------------
@app.on_event("startup")
def startup_event():
    print("[*] Starting scheduler thread...")
    threading.Thread(target=run_scheduler, daemon=True).start()


@app.get("/")
def root():
    return {"Welcome to Threat Harvester"}
