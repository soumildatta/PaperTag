from pdfquery import PDFQuery

filename = str(input("Enter the filename: "))
filename = '2201.08619.pdf'

pdf = PDFQuery(filename)
pdf.load()

text_elements = pdf.pq('LTTextLineHorizontal')

text = [t.text for t in text_elements]

index = text.index('')

title = ''.join(text[:index])

print(title)