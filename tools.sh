#!/bin/sh
case $1 of
    "start")
        cd /app
        pip install -r requirements.txt
        python main.py;;
    "restart")
        git pull
        docker restart nav;;
esac
