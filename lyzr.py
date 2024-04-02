# app.py
import requests
import json

LYZR_API_KEY = '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'

def transcribe_audio(audio_file_path):
    url = 'https://api.lyzr.io/transcribe'
    headers = {
        'Authorization': f'Bearer {LYZR_API_KEY}'
    }
    files = {'audio': open(audio_file_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        data = response.json()
        transcription = data['transcription']
        return transcription
    else:
        return None

