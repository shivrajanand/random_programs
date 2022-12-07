# pip install youtube_transcript_api

from youtube_transcript_api import YouTubeTranscriptApi

video_link = input("Paste the video link\n>>> ")
file_name = input("\nEnter the name of txt file in which you want to save subtitles\n>>> ")
video_id = video_link.split('watch?v=')[1]

subtitle = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=['en'])

# you can do anything with downloaded caption.
# for example:

file = open(file_name, "a")
subtitle = str(subtitle)
file.write(subtitle)
# print(subtitle)