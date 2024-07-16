#!/bin/sh
wget -O nav.zip https://github.com/jesongit/nav/archive/refs/heads/master.zip

unzip nav.zip -d .
mv nav-master/* .

rm -f nav.zip
rm -rf nav-master