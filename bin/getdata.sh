#!/bin/sh
python3 /home/robyn/capstone/splunk/etc/apps/Capstone/bin/python-fitbit-master/GetData.py
wait
wmctrl -a firefox
xdotool key Ctrl+w
