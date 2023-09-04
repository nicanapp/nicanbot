from youtube_transcript_api import YouTubeTranscriptApi

list = YouTubeTranscriptApi.get_transcript("video_youtube_id")

for i in list:
    print(f" {i['start']} : {i['text']}")