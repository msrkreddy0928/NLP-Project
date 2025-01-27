from flask import Flask,render_template,request,json
import pdfplumber
import os
import sys
sys.path.append('/home/shiva/Desktop/ML/Files/NLP/src')
from src.pipelines import pipeline
from src.mysqldb import update

app = Flask(__name__)

sno_=None


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/extract",methods=['POST'])
def feature_extraction():
    
    doc = request.files['file']
    
    sno,name,phoneNo,passOutYear,degree,college,yearsOfExp = pipeline(doc)
    global sno_
    sno_=sno
    
    return render_template('home.html',nameOut=name,phonenumOut=phoneNo,passoutOut=passOutYear,degreeOut=degree,collegeOut=college,expyearsOut=yearsOfExp)
    
    
@app.route("/save",methods=['POST'])
def save_modify_features():
    
    rows_aff = None
    data = request.get_json()
   
    rows_aff=update(sno_,data)
    
    print(rows_aff)
    
    return "ok"
    

if __name__=="__main__":
   app.run(host='192.168.10.130', port=5000)