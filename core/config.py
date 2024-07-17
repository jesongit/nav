#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests
from nicegui import ui

LINKS = []


def refresh_config(notify: bool = True):
    global LINKS
    data = get_config()
    LINKS = [(item['key'], item['name'], item['link']) for item in data['links']]
    if notify:
        ui.notify('刷新成功')


def get_config():
    response = requests.get('https://raw.githubusercontent.com/jesongit/nav/master/config.json')
    return json.loads(response.text)


def search_link(pattern: str):
    if not pattern:
        return LINKS
    return [(name, nick, link) for name, nick, link in LINKS if pattern in name]

