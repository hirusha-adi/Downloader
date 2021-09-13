# from pytube import *

# yt = YouTube("https://www.youtube.com/watch?v=Jk1lkVYbZ_c")
# # video = yt.streams.filter(progressive=True)
# video = yt.streams.filter(file_extension="mp3")
# print(video)

from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('Hirusha Adikari', limit = 1)
mainresult = videosSearch.result()["result"]
video_index = mainresult[0]


print(f"""
Type: {video_index["type"]}
Title: {video_index["title"]}
Publisehd Time: {video_index["publishedTime"]}
Duration: {video_index["duration"]}
View Count: {video_index["viewCount"]["text"]}
Video Thumbnail: {video_index["thumbnails"][0]["url"]}
Uploaded channel name: {video_index["channel"]["name"]}
Video Link: {video_index["link"]}
""")


