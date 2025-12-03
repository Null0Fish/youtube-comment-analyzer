import speech_recognition as sr
import textwrap


def convert_audio(video_id):
    recognizer = sr.Recognizer()

    with sr.AudioFile(f"./data/audio/raw_audio/{video_id}.wav") as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio)
    text = textwrap.fill(text, width=120)
    with open(f"./data/audio/processed_audio/{video_id}.txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)
