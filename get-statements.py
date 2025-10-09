#!/usr/bin/env python3
import json
import requests
from slugify import slugify

limit = 100
page = 0

response = requests.get(f'https://politiekereclame.nl/api/public/statements?page={page}&limit={limit}')
data = response.json()

while data['meta']['filter_count'] > (limit * page - 1):
  for item in data['items']:
    org = slugify(item['organization_created'].get('name', ''))
    name = slugify(item.get('name', ''))
    with open(f"items/{org}_{name}_{item['id']}.json", 'w') as OUT:
      json.dump(item, OUT, indent=2)
  page += 1
