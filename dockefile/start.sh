#!/bin/bash

folder="nav"

if [ ! -d "$folder" ]; then
    git clone xxx
fi

cd nav
git pull

python3 main.py