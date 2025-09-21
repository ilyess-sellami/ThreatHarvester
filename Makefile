# -------------------------------
# Threat Harvester Makefile
# -------------------------------

install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

clean:
	rm -rf __pycache__ *.pyc *.pyo
