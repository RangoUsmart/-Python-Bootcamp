
import csv
import PyPDF2

data = open('example.csv', encoding='utf-8')
print(data)
data_lines = list(data)
print(data_lines[0:3])

# ________________________________________

f = open('Working_Business_Proposal.pdf','rb')

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for p in range(len(pdf_reader.pages)):
    
    page = pdf_reader.pages[0]
    
    pdf_text.append(page.extract_text())
print(pdf_text[3])