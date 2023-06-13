#!/bin/bash

# Stop Firefox before deleting the history
firefox_pid=$(pgrep firefox)
if [ -n "$firefox_pid" ]; then
    echo "Stopping Firefox..."
    killall firefox
fi

# Delete the history searches
echo "Deleting Firefox history searches..."
rm -f ~/.mozilla/firefox/*/places.sqlite*

# Restart Firefox
if [ -n "$firefox_pid" ]; then
    echo "Starting Firefox..."
    firefox &
fi

