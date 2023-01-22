#!/usr/bin/env python3

import json
import requests
import argparse
from datetime import datetime

def get_alert_ads_from_page(page_index):
    url = f"https://api.jinka.fr/apiv2/alert/{alert_id}/dashboard?filter=all&page={page_index}&rrkey=xdwna9&sorting="

    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization":
            f"Bearer {authentication_token}",

    }
    response = requests.get(url, headers=headers)

    return response.json()

def get_last_page_index():
    first_page_response = get_alert_ads_from_page(1)
    
    return first_page_response['pagination']['nbPages']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alert_id", help="Alert ID to scrap", required=True)
    parser.add_argument("--authentication_token", help="Authentication token found in Chrome > Application > Cookies > LA_API_TOKEN", required=True)
    args = parser.parse_args()

    alert_id=args.alert_id
    authentication_token=args.authentication_token

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    print(f"Scraping Jinka for the alert {alert_id}...")
    last_page_index = get_last_page_index()
    print(f"{last_page_index} pages found !")
    ads = []

    for current_page_index in range (1, last_page_index + 1):
        print("Looping through page: ", current_page_index)
        current_page_data = get_alert_ads_from_page(current_page_index)
        current_page_ads = current_page_data['ads']
        ads = ads + current_page_ads

    output_file_name = f"data/jinka-{timestamp}.json"
    print(f"Saving to: {output_file_name}")
    pretty_json = json.dumps(ads, indent=4)

    with open(output_file_name, "a") as f:
        f.write(pretty_json)

if __name__ == "__main__":
    main()