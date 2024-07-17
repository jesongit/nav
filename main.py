#!/usr/bin/python
# -*- coding: UTF-8 -*-
from core.config import refresh_config
from nicegui import ui, app
from router import home

refresh_config()

app.include_router(home.router)
ui.page_title('Just Navigation')
ui.run()
