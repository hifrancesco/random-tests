from pytube import YouTube
import math
import time

# Function to display a progress bar
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')

    if iteration == total:
        print()

# Prompt the user to enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object and extract the video
try:
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
except Exception as e:
    print("Error:", str(e))
    exit()

# Download the video with progress bar
try:
    print("Downloading:", video.title)
    video.download(filename='video_temp')
    print("Download complete!")
except Exception as e:
    print("Error:", str(e))

# Simulate progress bar during download
file_size = video.filesize
chunk_size = 1024
progress = 0
iteration = 0
total_iterations = math.ceil(file_size / chunk_size)

# Simulate the progress bar while reading the file
with open('video_temp', 'rb') as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        progress += len(chunk)
        iteration += 1
        print_progress_bar(iteration, total_iterations, prefix='Progress:', suffix='Complete', length=30)

        # Simulating delay to show the progress bar
        time.sleep(0.1)

# Rename the temporary file to the video's original filename
import os
os.rename('video_temp', video.title + '.mp4')
