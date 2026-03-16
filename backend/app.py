from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

# CORS Configuration
CORS(app)

# Upload Folder Setup
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/health', methods=['GET'])
def health_check():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(debug=True)
