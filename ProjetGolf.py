from video import open_video



video_path = input("Enter video access path: ")

video = open_video(video_path)

if (video.isOpened()):
    print("Video successfully opened")
else:
    print("Error loading video")
