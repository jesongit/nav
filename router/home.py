#!/usr/bin/python
# -*- coding: UTF-8 -*-
from dataclasses import dataclass

from nicegui import APIRouter, ui
from nicegui.events import GenericEventArguments

from core.config import search_link, refresh_config
from core.data import SearchVo

router = APIRouter()


@router.page("/")
def home():
    search = SearchVo()

    @ui.refreshable
    def links():
        print('links')
        link_list = search_link(search.value)
        if not link_list:
            return
        with ui.row().classes('flex-center'):
            for _, name, link in link_list:
                with ui.link(target=link, new_tab=True):
                    ui.button(name).props('outline')

    def refresh():
        refresh_config()
        links.refresh()

    def handle_key(event: GenericEventArguments):
        if event.args['key'] == 'Enter':
            link_list = search_link(search.value)
            if not link_list:
                return
            ui.navigate.to(link_list[0][2], new_tab=True)
        elif event.args['key'] == 'Escape':
            search.value = ''
            links.refresh()

    with ui.row().classes('w-full justify-end'):
        ui.switch(on_change=lambda e: ui.dark_mode(e.value))
        ui.button(icon='refresh', on_click=refresh)

    with ui.row().classes('w-full self-center flex-center'), ui.column().classes('col-6'):
        ui.input(on_change=links.refresh). \
            props('outlined clearable').classes('w-full').bind_value(search).on('keydown', handle_key)
        links()
