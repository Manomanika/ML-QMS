# app.py

from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from models import db, CallRecord
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///call_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'your_secret_key'

db.init_app(app)

LYZR_API_KEY = 'YOUR_LYZR_API_KEY_HERE'
LYZR_API_URL = 'https://api.lyzr.ai/transcribe'

# Define KPI calculation function
def calculate_kpis(transcription):
    # Dummy KPI calculation, replace with actual logic
    words_count = len(transcription.split())
    return {'words_count': words_count}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        audio_file = request.files['file']
        if audio_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Save uploaded file
        filename = secure_filename(audio_file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + '/' + filename
        audio_file.save(file_path)

        # Send audio file to Lyzr AI for transcription
        files = {'file': open(file_path, 'rb')}
        headers = {'Authorization': f'Bearer {LYZR_API_KEY}'}
        response = requests.post(LYZR_API_URL, files=files, headers=headers)

        if response.status_code != 200:
            return jsonify({'error': 'Transcription failed'}), 500

        transcription = response.json().get('transcription')
        
        # Calculate KPIs
        kpis = calculate_kpis(transcription)

        # Store call record in database
        call_record = CallRecord(transcription=transcription, **kpis)
        db.session.add(call_record)
        db.session.commit()

        return jsonify({'transcription': transcription, 'kpis': kpis}), 200

    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
