#!/bin/bash

gnome-terminal -x bash -c "yt-dlp -x --audio-format mp3 -a list -o 'music/%(title)s.%(ext)s'"
