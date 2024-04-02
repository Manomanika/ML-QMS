
from flask import Flask, request, render_template
import zipfile
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = 'calls.zip'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Extract the zip file
        with zipfile.ZipFile(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(app.config['UPLOAD_FOLDER'], 'extracted_calls'))
        
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
