from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.invoice_processor import InvoiceProcessor

upload_bp = Blueprint('upload', __name__)
processor = InvoiceProcessor()
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'No file selected or wrong type'}), 400
    filename = secure_filename(file.filename)
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath

    if filename.lower().endswith('.pdf'):
        text = processor.extract_text_from_pdf(filepath)
    else:
        text = processor.extract_text_from_image(filepath)
    invoice_data = processor.extract_invoice_data(text)

    return jsonify({'filename': filename, 'data': invoice_data})