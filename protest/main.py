
from pathlib import Path
from uuid import uuid4

import qrcode
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data"

        
class PdfParser:
    """
        Set pdf file path qrcode image into pdf file
    """
    def __init__(self, file):
        self.file = DATA_PATH / file
        self.reader = PdfReader(self.file)

    def page_spliter(self):
        """
            Split pdf file into page 
        """
        yield from range(len(self.reader.pages))

    def create_pdf(self, save_folder_path, page):
        """
            Create pdf file with qrcode image
        """
        # Get the watermark file you just created

        SAVED_FILE_PATH = DATA_PATH / save_folder_path / f"{page}.pdf"

        writer = PdfWriter()
        
        with open(SAVED_FILE_PATH, "wb") as file:
            # create qrcode image
            qr_code_image = self.create_qrcode_image(SAVED_FILE_PATH)
            # create qrcode pdf file
            watermark_file = self.create_qrcode_pdf(qr_code_image=qr_code_image)
            watermark = PdfReader(open(watermark_file, "rb"))
            self.reader.pages[page].merge_page(watermark.pages[0]) # merge qrcode pdf file to pdf file
            # add qrcode image to pdf file
            writer.add_page(self.reader.pages[page]) # add page to pdf file
            writer.write(file) # write pdf file
            
    def create_qrcode_image(self, save_folder_path):
        qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=3,
        )
        qr_code.add_data(save_folder_path)
        qr_code.make(fit=True)
        qr_code_image = qr_code.make_image(fill_color="black", back_color="white")
        qr_code_image.save(DATA_PATH / "data.png")
        return DATA_PATH / "data.png"


    def create_qrcode_pdf(self,  qr_code_image, watermark_file:str='watermark.pdf'):
        """
            Create pdf file with qrcode image
        """
        # if watermark_file doesn't exist, create it
        watermark_file = DATA_PATH / watermark_file
        if not watermark_file.exists():
            watermark_file.touch()

        doc = Canvas(str(DATA_PATH / watermark_file))
        # draw the QR code at the specified coordinates
        doc.drawImage(qr_code_image, 295, 95)
        doc.save()
        return watermark_file
        
if __name__ == "__main__":
    new_folder = DATA_PATH / f"folder_{uuid4().hex[:8]}"
    new_folder.mkdir()

    pdf_file = PdfParser("data_file.pdf")
    for page in pdf_file.page_spliter():
        pdf_file.create_pdf(save_folder_path=new_folder, page=page)

#TODO: Optimize code using multiprocessing or threading, asynchronus programming