import speech_recognition as sr

# Define the audio file path
audio_file_path = "C:\\Users\\MANOJ RK\\Downloads\\sample_call_.wav"

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Recognize the audio using Google Speech Recognition
try:
    transcript = recognizer.recognize_google(audio_data)
    print("Transcript:", transcript)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
