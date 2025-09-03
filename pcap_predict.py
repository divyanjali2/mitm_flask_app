
import requests

API_URL = 'http://127.0.0.1:8000/predict'
PCAP_FILE = 'synthetic_flows1.pcap'

with open(PCAP_FILE, 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.strip().strip(',') 
    line = line.strip('[]')         
    if not line:
        continue
    features = [float(x.strip()) for x in line.split(',')]
    print(f"Extracted features from line {i}:", features)

    # Send to API
    try:
        response = requests.post(API_URL, json={"features": features})
    except requests.RequestException as e:
        print("API request failed:", e)
        continue

    if response.status_code == 200:
        result = response.json()
        label = result.get("label", "").lower()
        attack_prob = result.get("attack_probability", 0)
        attack_percent = attack_prob * 100  # convert to percentage

        if label == "attack" or attack_prob > 0.5:
            print(f"🚨 ATTACK detected (probability: {attack_percent:.2f}%)")
        else:
            print(f"✅ Normal traffic (probability: {attack_percent:.2f}%)")
    else:
        print("API request failed with status:", response.status_code)
