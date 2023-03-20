from PyPDF2 import PdfReader

pdf_list=[]
def pdffile(file):
    reader=PdfReader(file)
    for page in reader.pages:
        pdf_list.append(page.extract_text())
    print(pdf_list[1])
        


if __name__ == '__main__':
    pdffile('data/file.pdf')

