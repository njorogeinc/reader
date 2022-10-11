from flask import Flask, render_template, request, url_for, flash, redirect
import pyPDF2
import pyttsx3

app = Flask(__name__)
app.config['SECRET_KEY'] = '5e979b170e38298397c45bb514d7a5fab744166fb5834ab4'

@app.route("/", method=('POST'))
def hello_world():
    
    for request.method == 'POST':
        title = request.form['inputPassword']
        
        pdfobj = open(title, 'rb')

        pdfreader = pyPDF2.PdfFileReader(pdfobj)

        text = ""

        for pagenumber in range(pdfreader.numPages):
            page = pdfreader.getPage(pagenumber)
            text += page.extractText()

        pdfobj.close()

        print(text)

        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

           
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)