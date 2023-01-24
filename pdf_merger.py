import PyPDF2
import sys
import os
# create a merger object
merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    print(f"Current file being handled is {file}")
    if file.endswith(".pdf"):
        print("FOund a pdf and going to use it now")
        merger.append(file)
    merger.write("mergedFiles.pdf")
