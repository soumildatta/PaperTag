from pdfquery import PDFQuery

pdf = PDFQuery('2201.08619.pdf')
pdf.load()

text_elements = pdf.pq('LTTextLineHorizontal')

text = [t.text for t in text_elements]

print(text)