#!/bin/bash

# Create directories to store the different file types
mkdir -p ~/Desktop/Documents
mkdir -p ~/Desktop/Music
mkdir -p ~/Desktop/Pictures
mkdir -p ~/Desktop/Videos
mkdir -p ~/Desktop/Other

# Move files to the appropriate folders
find ~/Desktop -maxdepth 1 -type f -print0 | while read -d $'\0' file
do
    case "$(file -b --mime-type "$file")" in
        "application/pdf")      mv "$file" ~/Desktop/Documents/ ;;
        "audio/mpeg"|"audio/flac"|"audio/ogg"|"audio/wav"|"audio/x-ms-wma") mv "$file" ~/Desktop/Music/ ;;
        "image/jpeg"|"image/png"|"image/gif"|"image/svg+xml"|"image/tiff"|"image/bmp") mv "$file" ~/Desktop/Pictures/ ;;
        "video/mp4"|"video/x-msvideo"|"video/x-flv"|"video/x-matroska"|"video/quicktime"|"video/x-ms-wmv") mv "$file" ~/Desktop/Videos/ ;;
        *)                      mv "$file" ~/Desktop/Other/ ;;
    esac
done

echo "Done sorting files on Desktop."
