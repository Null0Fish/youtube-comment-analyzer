from pytube import YouTube
from pydub import AudioSegment
import os


def fetch_audio(video_id):
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_path = audio_stream.download(output_path=".", filename="temp_audio")
    audio = AudioSegment.from_file(audio_path)
    os.remove(audio_path)
    output_audio_file = f"./data/audio/raw_audio/{video_id}.wav"
    audio.export(output_audio_file, format="wav")
