#!/usr/bin/env python3

import json
import requests
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

url = "https://api.jinka.fr/apiv2/alert/2306da5e990d75bb2e00a0ea2381f63c/dashboard?filter=all&page=1&rrkey=xdwna9&sorting="

headers = {
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization":
        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTMzMzgxLCJlbWFpbCI6ImFudG9ueS52ZW9wYXNldXRoQGVwZmVkdS5mciIsImNyZWF0ZWRfYXQiOiIyMDIzLTAxLTIyVDA5OjMzOjUzLjAwMFoiLCJpYXQiOjE2NzQzODQ1NjIsImV4cCI6MTY3Njk3NjU2Mn0.iAcn9knYNqxVPsM-lxUVqThS5rLzIjDwnohNVrn5OeI",

}
# Trigger curl request
response = requests.get(url, headers=headers)

data = response.json()

# Write JSON data to file
with open(f"jinka-{timestamp}.json", "a") as f:
    json.dump(data, f)
