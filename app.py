
import streamlit as st
import zipfile
import assemblyai as aai
from textblob import TextBlob

# Function to extract MP3 files from a zip file
def extract_audio_from_zip(zip_file):
    files = []
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        list = zip_ref.namelist()
        # Filter only MP3 files
        mp3_files = [file for file in list if file.endswith('.mp3')]
        # Extract MP3 files
        for mp3_file in mp3_files:
            zip_ref.extract(mp3_file)
            files.append(mp3_file)
    return files

# Function to transcribe audio file using AssemblyAI
def transcribe_mp3(audio_file, api_key):
    aai.settings.api_key = api_key
    transcriber = aai.Transcriber()

    try:
        transcript = transcriber.transcribe(audio_file)
        return transcript.text
    except Exception as e:
        st.error(f"Transcription failed: {e}")
        return None
def anlyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity < 0:
        return "Satisfied"
    elif polarity > 0:
        return "Dissatisfied"
    else :
        return "Neutral"
# Streamlit UI
def main():
    st.title("Audio Transcription ")
    st.write("Please upload a zip file containing MP3 files.")

    # File uploader widget
    zip_file = st.file_uploader("Upload Zip File", type=['zip'])

    if zip_file is not None:
        # Extract MP3 files from the uploaded zip file
        files = extract_audio_from_zip(zip_file)

        # API key (replace with your actual API key)
        api_key = "3bcc317f606d407cb0dd720c52005e41"

        if files:
            st.write("MP3 files extracted successfully:")
            for file in files:
                st.write(file)

            # Transcribe each MP3 file
            st.write("Transcriptions:")
            for mp3_file in files:
                transcription = transcribe_mp3(mp3_file, api_key)
                if transcription:
                    st.write(f"{mp3_file}: {transcription}")

                    sentiment = anlyze_emotion(transcription)
                    st.write(f"Sentiment for {mp3_file}: {sentiment}")
                else:
                    st.write(f"{mp3_file}: Transcription failed")

if __name__ == "__main__":
    main()
