import pytesseract
from PIL import Image
import pdf2image

class InvoiceProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""

    def convert_pdf_to_images(self):
        # Convert PDF to images
        return pdf2image.convert_from_path(self.file_path)

    def ocr_images(self, images):
        # Perform OCR on each image and store the results
        for image in images:
            self.text += pytesseract.image_to_string(image) + '\n'

    def extract_data(self):
        # Example logic to extract invoice details from text
        invoice_data = {}
        lines = self.text.split('\n')
        for line in lines:
            if "Invoice Number:" in line:
                invoice_data['invoice_number'] = line.split(":")[-1].strip()
            elif "Total Amount:" in line:
                invoice_data['total_amount'] = line.split(":")[-1].strip()
        return invoice_data

    def process_invoice(self):
        images = self.convert_pdf_to_images()
        self.ocr_images(images)
        return self.extract_data()