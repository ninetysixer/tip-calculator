import pyttsx3
import pdfplumber
import PyPDF2

file = 'C:/Users/TR/Desktop/ornekPDF.pdf'

# Creating a PDF File Object
pdfFileObj = open(file, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Get the number of pages
pages = len(pdfReader.pages)

with pdfplumber.open(file) as pdf:
    # Loop through the number of pages
    for i in range(0, pages): 
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
