#!/usr/bin/python

from subprocess import call
import os
import time

WP_PATH = "/home/bjoern/Pictures/Wallpaper"
TIMER = 60

wallpaper = []

for file in os.listdir(WP_PATH):
    if file.endswith(".jpg") or file.endswith(".png"):
        wallpaper.append(file)

i = 0;
while True:
    fileURI = "file://" + WP_PATH + "/" + wallpaper[i]

    print fileURI

    call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", fileURI])

    i = (i + 1) % len(wallpaper)
    time.sleep(TIMER)
