#!/usr/bin/env python3
import json
import requests

limit = 100
page = 0

response = requests.get(f'https://politiekereclame.nl/api/public/statements?page={page}&limit={limit}')
data = response.json()

while data['meta']['filter_count'] > (limit * page - 1):
  for item in data['items']:
    with open(f"items/{item['id']}.json", 'w') as OUT:
      json.dump(item, OUT, indent=2)
  page += 1
