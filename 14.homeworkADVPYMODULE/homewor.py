'''
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file,
open it, and search for a telephone number.
Good luck!
'''
import os
import re
pattern = r'\d{3}-\d{3}-\d{4}'
for folder, subfolders, files in os.walk("extracted_content"): 
    for file in files:
        with open(os.path.join(folder, file), 'r') as file:
            file_content = file.read()
        phone=re.findall(pattern,file_content)
        if phone:
            print(f"\t{phone[0]}")