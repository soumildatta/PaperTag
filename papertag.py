from pdfquery import PDFQuery
import os

def _extract_pdf_title(pdf_path):
    pdf = PDFQuery(pdf_path)
    pdf.load()

    text_elements = pdf.pq('LTTextLineHorizontal')  
    text = [t.text for t in text_elements]
    index = text.index('')
    title = ''.join(text[:index]).strip().split('@')[0].replace('.', '_')

    if title == '':
        title = pdf_path.split('/')[-1].replace('.pdf', '')
        return title, False

    return title, True
    
# print(_extract_pdf_title('.pdf'))

def rename_pdf_file(pdf_path):
    title, changed = _extract_pdf_title(pdf_path)
    new_file_name = f'{title}.pdf'

    if changed:
        path = os.path.join(os.path.dirname(pdf_path), new_file_name)
        os.rename(pdf_path, path)
        print(f"File {pdf_path} renamed to {new_file_name}")
    else:
        print(f"No title parsed for {pdf_path}. Skipping...")

if __name__ == '__main__':
    scan_dir = str(input("Enter the directory path to scan: "))

    # list all pdf files in scan_dir
    pdf_files = [f for f in os.listdir(scan_dir) if f.endswith('.pdf')]

    print(f"Found {len(pdf_files)} pdf files in {scan_dir}")
    print("Starting to rename files...")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(scan_dir, pdf_file)
        rename_pdf_file(pdf_path)