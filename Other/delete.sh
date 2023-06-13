#!/bin/bash

echo "Deleting Firefox browsing history..."

Stop Firefox if it is running
if pgrep firefox >/dev/null; then
    echo "Stopping Firefox..."
    osascript -e 'quit app "Firefox"'
    sleep 5 # Wait for Firefox to fully exit
fi

# Delete the places.sqlite file from the Firefox profile folder
rm -f ~/Library/Application\ Support/Firefox/Profiles/*/places.sqlite*

echo "Firefox browsing history has been deleted."

# Shut down all other running applications
echo "Shutting down other applications..."
osascript -e 'tell application "System Events" to set the visible of every process whose name is not "Finder" and name is not "Terminal" to false'

# Shut down the MacBook
echo "Shutting down MacBook..."
sudo shutdown -h now