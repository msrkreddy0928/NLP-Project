from flask import Flask,render_template,request
import pdfplumber
import os
import sys
sys.path.append('/home/shiva/Desktop/ML/Files/NLP/src')
import pdf_text_extraction

from src.pipelines import pipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/extract",methods=['POST'])
def feature_extraction():
    
    doc = request.files['file']
    
    name,phone_num,years_of_exp,passout,qualification = pipeline(doc)
    
    return render_template('home.html',nameOut=name,phonenumOut=phone_num,passoutOut=passout,qualificationOut=qualification,expyearsOut=years_of_exp)
    
    




if __name__=="__main__":
   app.run(host='192.168.10.130', port=5000)