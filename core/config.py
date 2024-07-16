#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests


def get_config():
    proxies = {
        # 'http': 'http://127.0.0.1:7890',
        # 'https': 'http://127.0.0.1:7890',
    }
    response = requests.get('https://raw.githubusercontent.com/jesongit/nav/master/config.json', proxies=proxies)
    return json.loads(response.text)


def search_link():
    pass
