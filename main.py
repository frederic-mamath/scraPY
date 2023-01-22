#!/usr/bin/env python3

import json
import requests
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--alert_id", help="Alert ID to scrap")
parser.add_argument("--authentication_token", help="Authentication token found chrome/Application/Cookies/LA_API_TOKEN")
args = parser.parse_args()

alert_id=args.alert_id
authentication_token=args.authentication_token

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

url = f"https://api.jinka.fr/apiv2/alert/{alert_id}/dashboard?filter=all&page=1&rrkey=xdwna9&sorting="

headers = {
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization":
        f"Bearer {authentication_token}",

}
response = requests.get(url, headers=headers)

data = response.json()

with open(f"data/jinka-{timestamp}.json", "a") as f:
    json.dump(data, f)
