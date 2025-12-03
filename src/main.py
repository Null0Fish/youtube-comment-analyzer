import time
import os
from src.comment_handling.comment_cleaner import clean_comments
from src.comment_handling.comment_fetcher import fetch_comments
from src.entity_handling.entity_sentiment_finder import find_entity_sentiment
from src.entity_handling.entity_sentiment_cleaner import clean_entity_sentiments
from src.audio_handeling.audio_featcher import fetch_audio
from src.audio_handeling.audio_converter import convert_audio


def main():
    start_time = time.time()
    video_id = 'p15xzjzR9j0'
    fetch_comments(video_id)
    clean_comments(video_id)
    find_entity_sentiment(video_id)
    clean_entity_sentiments(video_id)
    fetch_audio(video_id)
    convert_audio(video_id)
    elapsed_time = time.time() - start_time
    print(f"Time taken to analyze comments: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    ffmpeg_path = "C:\\Users\\Me\\Documents\\ffmpeg-6.1-essentials_build\\bin\\ffmpeg.exe"
    ffprobe_path = "C:\\Users\\Me\\Documents\\ffmpeg-6.1-essentials_build\\bin\\ffprobe.exe"
    os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
    os.environ["PATH"] += os.pathsep + os.path.dirname(ffprobe_path)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './credentials/service_account_key.json'
    main()
