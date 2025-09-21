# Threat Harvester

...

---

## Overview
**Threat Harvester** is an open-source Threat Intelligence **IoC (Indicators of Compromise)** collector designed for SOC teams, security researchers, and startups. This tool **fetches IoCs from multiple threat intelligence platforms** daily, normalizes them, and stores them in **Elasticsearch** for visualization in **Kibana**.

---

## Key Features

- Fetches new or updated IoCs **every 24 hours**.
- **Normalizes IoCs** with metadata such as type, TLP, tags, source, and pulse/campaign info.
- Supports **multiple threat intelligence sources** (OTX AlienVault, MISP, etc.).
- Stores IoCs in **Elasticsearch** for **fast querying and analytics**.
- **Kibana** dashboards for **filtering and visualizing IoCs**.
- **Dockerized** setup with automatic Elasticsearch and Kibana deployment.

## Architecture Overview

...

**Workflow:**
1. **Every 24 hours**, the FastAPI background scheduler fetches IoCs created or updated in the last day.
2. IoCs are normalized and stored in Elasticsearch.
3. Kibana provides dashboards to filter, search, and visualize IoCs by type, source, TLP, and other attributes.

---

## Getting Started

### Requirements

- Docker & Docker Compose
- Python 3.11+

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ilyess-sellami/ThreatHarvester.git
cd ThreatHarvester
```

2. Open `.env` file and set your API keys:
```env
OTX_API_KEY=""
ABUSEIPDB_API_KEY=""
```

3. Build and run the project with Docker Compose:
```bash
docker-compose up -d
```
- Elasticsearch and Kibana will be automatically installed.
- The FastAPI fetcher runs in the background and pulls IoCs every 24 hours.

### Access Kibana

- Kibana Dashboard: `http://localhost:5601`
- Default Elasticsearch URL: `http://localhost:9200`
