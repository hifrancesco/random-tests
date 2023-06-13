from pytube import YouTube

# Prompt the user to enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object and extract the video
try:
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
except Exception as e:
    print("Error:", str(e))
    exit()

# Download the video
try:
    print("Downloading:", video.title)
    video.download()
    print("Download complete!")
except Exception as e:
    print("Error:", str(e))
