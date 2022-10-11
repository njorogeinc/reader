from flask import Flask, render_template, request
import pyPDF2
import pyttsx3

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    
    if request.method == "POST":
        title = request.form.get('inputPassword')
        
        pdfobj = open(title, 'rb')

        pdfreader = pyPDF2.PdfFileReader(pdfobj)

        text = ""

        for pagenumber in range(pdfreader.numPages):
            page = pdfreader.getPage(pagenumber)
            text += page.extractText()

        pdfobj.close()

        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

           
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)