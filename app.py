from flask import Flask
from flask import request
import uuid
from os import path
import os
import json

from classifier import Classifier

app = Flask(__name__)

base_dir = path.join('.')
tmp_dir = path.join(base_dir, 'tmp')
if not path.exists(tmp_dir):
    os.mkdir(tmp_dir)
model_path = path.join(base_dir, 'model', 'classifier.h5')
classifier = Classifier(model_path)


@app.route('/classify', methods=['POST'])
def classify():
    f = request.files['image']
    try:
        ext = path.splitext(f.filename)[1]
        unique_filename = str(uuid.uuid4()) + ext
        file_path = path.join(tmp_dir, unique_filename)
        f.save(file_path)
        t, confidence = classifier.predict(file_path)
        os.remove(file_path)
        return json.dumps({
            'class': t,
            'confidence': float(confidence),
        })
    except Exception as e:
        return json.dumps({
            'error': str(e)
        })
