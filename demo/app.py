from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

'''import pyPDF2
import pyttsx3

file_to_read = input("Please enter file name:")

 pdfobj = open(file_to_read, 'rb')

 pdfreader = pyPDF2.PdfFileReader(pdfobj)

 text = ""

 for pagenumber in range(pdfreader.numPages):
    page = pdfreader.getPage(pagenumber)
    text += page.extractText()

pdfobj.close()

print(text)

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()'''

