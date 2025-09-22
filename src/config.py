import os
from datetime import datetime

OUTPUT_DIR = os.path.abspath("outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_output_file(platform: str, module: str = None) -> str:
    """
    Generate output file path for IOCs.
    
    Args:
        platform (str): Name of the platform (e.g., 'linux', 'windows', 'mac').
        module (str): Optional module name (e.g., 'urlhaus', 'malwarebazaar').
        
    Returns:
        str: Full path of the output file.
    """
    today_str = datetime.utcnow().strftime("%Y-%m-%d")

    if module:
        filename = f"iocs_{platform}_{module}_{today_str}.json"
    else:
        filename = f"iocs_{platform}_{today_str}.json"

    return os.path.join(OUTPUT_DIR, filename)

