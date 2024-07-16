#!/usr/bin/python
# -*- coding: UTF-8 -*-
from core.config import LINKS
from core.data import SearchVo
from nicegui import ui


@ui.page('/')
def home():
    search = SearchVo()

    @ui.refreshable
    def links():
        pattern = search.value
        link_list = LINKS if not pattern else [(name, nick, link) for name, nick, link in LINKS if pattern in name]
        if not link_list:
            return
        with ui.row():
            for _, nick, link in link_list:
                ui.button(nick, on_click=lambda: ui.navigate.to(link, new_tab=True)).props('outline')

    with ui.row().classes('w-full self-center flex-center'), ui.column().classes('col-6'):
        ui.input(on_change=links.refresh).props('outlined clearable').classes('w-full').bind_value(search)
        links()


ui.run()
