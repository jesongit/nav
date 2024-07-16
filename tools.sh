#!/bin/bash

case "$1" in
    "run")
        git pull
        python3 main.py;;
    "init")
        curl -L https://gitee.com/RubyMetric/chsrc/releases/download/pre/chsrc-x64-linux -o chsrc
        chmod +x ./chsrc
        ./chsrc set pip first
        ./chsrc set debian first
        git clone git@github.com:jesongit/nav.git .
esac