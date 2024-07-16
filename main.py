#!/usr/bin/python
# -*- coding: UTF-8 -*-
from core.config import get_config
from core.data import SearchVo
from nicegui import ui

LINKS = []


def refresh_config():
    global LINKS
    json = get_config()
    LINKS = [(item['key'], item['name'], item['link']) for item in json['links']]


refresh_config()


@ui.page('/')
def home():
    search = SearchVo()

    @ui.refreshable
    def links():
        global LINKS
        pattern = search.value
        link_list = LINKS if not pattern else [(name, nick, link) for name, nick, link in LINKS if pattern in name]
        if not link_list:
            return
        with ui.row():
            for _, nick, link in link_list:
                ui.button(nick, on_click=lambda: ui.navigate.to(link, new_tab=True)).props('outline')

    def refresh():
        refresh_config()
        links.refresh()

    ui.button(icon='refresh', on_click=refresh)

    with ui.row().classes('w-full self-center flex-center'), ui.column().classes('col-6'):
        ui.input(on_change=links.refresh).props('outlined clearable').classes('w-full').bind_value(search)
        links()


ui.run()
