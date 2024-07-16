#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests


def get_config():
    response = requests.get('https://raw.githubusercontent.com/jesongit/nav/master/config.json')
    return json.loads(response.text)


def search_link():
    pass
