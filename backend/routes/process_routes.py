from flask import Blueprint, request, jsonify
import csv
import os

process_bp = Blueprint('process', __name__)

@process_bp.route('/approve', methods=['POST'])
def approve_invoice():
    data = request.json
    return jsonify({'message': 'Invoice approved', 'invoice': data}), 200

@process_bp.route('/flag', methods=['POST'])
def flag_invoice():
    data = request.json
    return jsonify({'message': 'Invoice flagged for review', 'invoice': data}), 200

@process_bp.route('/export-csv', methods=['POST'])
def export_csv():
    invoices = request.json.get('invoices', [])
    output_file = 'exports/tally_export.csv'
    os.makedirs('exports', exist_ok=True)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Invoice Number', 'Vendor', 'Date', 'Total'])
        for invoice in invoices:
            writer.writerow([
                invoice.get('invoiceNumber', ''),
                invoice.get('vendor', ''),
                invoice.get('date', ''),
                invoice.get('total', 0)
            ])
    return jsonify({'message': 'CSV exported', 'file': output_file})