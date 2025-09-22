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
1. **Every 24 hours**, the scheduler fetches IoCs created or updated in the last day.
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
ABUSE_CH_API_KEY=""
```

3. Build and run the project with Docker Compose:
```bash
docker-compose up -d
```
- This will automatically start three services:
    - **ThreatHarvester**
    - **Elasticsearch**
    - **Kibana**

4. Verify that all containers are running:
```bash
docker ps
```
You should see something like this:

![Docker ps](/screenshots/docker_ps.png)

### Access Kibana

- Default Elasticsearch URL: `http://localhost:9200`

![Elasticsearch URL](/screenshots/elasticsearch_url.png)

- Kibana Dashboard: `http://localhost:5601`

![Kibana Dashboard](/screenshots/kibana_dashboard.png)

### Setting up the Data View

1. Open Kibana at `http://localhost:5601`. 

2. Go to **Stack Management → Data Views → Create Data View**.

![Create Data View](/screenshots/kibana_create_data_view.png)

3. Set the following:
    - Name: `Threat Harvester`
    - Index pattern: `threatharvester`
    - Time field: `@timestamp`

![Create Data View Form](/screenshots/kibana_create_data_view_form.png)

4. Click **Create Data View**.

### Exploring IoCs

- Go to **Discover** in Kibana to explore the collected IoCs.

![Kibaa Discover](/screenshots/kibana_discover.png)

- There are **many fields** you can use to **search or filter the IoCs**, such as `source`, `indicator`, `type`, `reporter`, `tags`, and `@timestamp`.

- For example you can filter or search by the **source** field:

```bash
source:"OTX"
```

![Kibana Filter Data with source](/screenshots/kibana_dashboard_filter_data_source.png)

The IoCs in Elasticsearch come from 4 sources: OTX, MalwareBazaar - abuse.ch, URLhaus - abuse.ch, and AbuseIPDB.

- You can also search by a specific **indicator**:

```bash
indicator:"301b905eb98d8d6bb559c04bbda26628a942b2c4107c07a02e8f753bdcfe347c"
```

![Kibana Filter Data with indicator](/screenshots/kibana_dashboard_filter_data_indicator.png)


---

## Conclusion

**Threat Harvester** is a comprehensive, automated Threat Intelligence platform that streamlines the collection, normalization, and analysis of Indicators of Compromise (IoCs). By integrating multiple reputable sources—OTX AlienVault, MalwareBazaar, URLhaus, and AbuseIPDB—it provides SOC teams, security researchers, and cybersecurity professionals with a centralized repository of actionable threat data.

The platform leverages **Elasticsearch** for fast, scalable storage and querying, and **Kibana** for intuitive visualization, enabling users to quickly detect, investigate, and respond to threats. Its fully **Dockerized deployment** ensures a reproducible, low-maintenance setup, making it suitable for both testing and production environments.

Overall, **Threat Harvester** simplifies threat intelligence aggregation, enhances situational awareness, and empowers organizations to proactively defend against evolving cyber threats.
