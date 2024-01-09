import csv
import PyPDF2
import re

data = open('Exercise_Files/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)
pattern = r'\d{3}.\d{3}.\d{4}'
link_str = ''

for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]
print(link_str)

f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfReader(f)
 
for n in range(len(pdf.pages)):
    
    page  = pdf.pages[n]
    page_text = page.extract_text()
    match = re.search(pattern,page_text)
    
    if match:
        print(match.group())