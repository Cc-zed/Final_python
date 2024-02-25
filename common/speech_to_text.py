# import speech_recognition as sr

# def speech_to_text(audio_file):
#     recognizer = sr.Recognizer()
    
#     with sr.AudioFile(audio_file) as source:

#         audio_data = recognizer.record(source)
        
#         try:
#             text = recognizer.recognize_google(audio_data)
#             return text
#         except sr.UnknownValueError:
#             print("Google Web Speech API could not understand the audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Web Speech API; {e}")

#     return None

# audio_path = ''
# audio_file = audio_path
# result = speech_to_text(audio_file)
# if result:
#     print("Text:", result)