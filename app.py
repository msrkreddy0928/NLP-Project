from flask import Flask,render_template,request,json,jsonify
import pdfplumber
import os
import sys
sys.path.append('/home/shiva/Desktop/ML/Files/NLP/src')
from src.pipelines import pipeline_start
from src.mysqldb import update,insert_all,retrive_all
from flask_cors import CORS
app = Flask(__name__)


CORS(app)


@app.route("/")
def home():
    
    return "HII"
    # return render_template('home.html')


@app.route("/extract",methods=['POST'])
def feature_extraction():
    
    doc = request.files['file']
   
    
    name,phoneNo,countryCode,degree1,degree2,passOutYear1,passOutYear2,college1,college2,yearsOfExp,summary = pipeline_start(doc)
    
    if degree1 is None:
        degree1=degree2
        passOutYear1=passOutYear2
        college1=college2
        degree2=None
        passOutYear2=None
        college2=None 
     
    percentage1=None
    percentage2 = None
    
    deg_list = {"degree2":degree2,"college2":college2,"passOutYear2":passOutYear2,"percentage2":percentage2}
 
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"degree":degree1,"deg2list":deg_list,"passOutYear1":passOutYear1,"college":college1,"yearsOfExp":yearsOfExp,"pecentage1":percentage1,"summary":summary}
    
    return jsonify(dict), 200 
    
 
 
 

     
@app.route("/values", methods=['POST'])
def save_features():
    data= request.json
    
    print(data)


    message = insert_all(data.get("name"),data.get("phoneNo"),data.get("countryCode"),data.get("email"),data.get("jobTitle"),data.get("organization"),data.get("yearsOfExp"),data.get("degree1"),data.get("degree2"),data.get("passOutYear1"),data.get("passOutYear2"),data.get("college1"),data.get("College2"),data.get("summary"),data.get("percentage1"),data.get("percenatge2"),data.get("pl"),data.get("fs"),data.get("bs"),data.get("ds"),data.get("os"))
 
    dic ={"message":message}
    return jsonify(dic  ) 




@app.route("/getdata", methods=['POST'])
def retrive_features():
    data= request.json
    
    print(data.get("phoneNo"))
    
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,percenatge1,percentage2,pl,fs,bs,ds,os= retrive_all(data.get("phoneNo")) 
    print("org",organization)
    
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"oraganization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":os}
    
    return jsonify(dict)

    

@app.route("/save",methods=['POST'])
def save_modify_features():
    
    rows_aff = None
    data = request.get_json()
    sno_=0
    rows_aff=update(sno_,data)
    
    print(rows_aff)
    
    return "ok"
    

if __name__=="__main__":
   app.run(host='192.168.10.130', port=5000)