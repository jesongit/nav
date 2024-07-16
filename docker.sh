#!/bin/bash
git pull
docker run -itd --name nav -p 8080:8080 -v ./:/app python:3.11-alpine sh /app/start.sh