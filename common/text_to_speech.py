import gtts
import os

def text_to_sp(text):
    tts = gtts.gTTS(text, lang='en')
    audio_path = 'message.mp3'
    tts.save(audio_path)
    if os.path.exists(audio_path):
        print("Audio file was created successfully")
        return audio_path
    else:
        print("Failed to create audio file")
        return None