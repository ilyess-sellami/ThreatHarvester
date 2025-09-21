from fastapi import FastAPI
from src import fetch_OTX_Alientvalut_IOCs
import schedule
import time
import threading

app = FastAPI(title="Threat Harvester")

# ---------------- Scheduler Job ----------------
def job():
    print("[*] Running daily OTX fetch...")
    fetch_OTX_Alientvalut_IOCs()

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
