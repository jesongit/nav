#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time

import requests

LINKS = []


def refresh_config():
    global LINKS
    while True:
        response = requests.get('https://example.com/config.json')
        data = json.loads(response.text)
        LINKS = [(item['key'], item['name'], item['link']) for item in data['links']]
        time.sleep(60)
