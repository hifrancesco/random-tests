from pytube import Playlist, YouTube


def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')


play_list = Playlist("https://www.youtube.com/watch?v=wcLmOu-FzyA")
print(play_list)
for p in play_list:
    print(p)
    yt = YouTube(p, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution().download('E:/video')
    print('\n')
