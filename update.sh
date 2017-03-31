#!/usr/bin/env bash
pkill -9 -f ReactBot.py
git pull origin master
python3 ReactBot.py