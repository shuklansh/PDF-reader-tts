import pyttsx3
import PyPDF2

readfunc = pyttsx3.init()
enterloc="enter the location of the pdf file you want me to read"
readfunc.say(enterloc)
readfunc.runAndWait()
location=input(r'')
book = open(location,'rb')

pdfread = PyPDF2.PdfFileReader(book)
pages=pdfread.numPages
print(pages)


for num in range(0, pages):
    page = pdfread.getPage(num)
    text = page.extractText()
    readfunc.say(text)
    readfunc.runAndWait()