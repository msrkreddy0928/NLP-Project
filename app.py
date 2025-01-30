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
   
    
    name,phoneNo,degree1,degree2,passOutYear,college1,college2,yearsOfExp,summary = pipeline_start(doc)
    
    passOutYear2=None
    percentage=None
    
    deg_list = {"degre2":degree2,"college2":college2,"passOutYear":passOutYear2,"percentage":percentage}
 
    dict ={"name":name,"phoneNo":phoneNo,"passOutYear":passOutYear,"degree1":degree1,"degree2":deg_list,"college":college1,"yearsOfExp":yearsOfExp,"summary":summary}
    
    return jsonify(dict), 200 
    
 
 
 

     
@app.route("/values", methods=['POST'])
def save_features():
    data= request.json
    
    print(data)


    message = insert_all(data.get("name"),data.get("phoneNo"),data.get("email"),data.get("jobTitle"),data.get("currentOrganization"),data.get("yearsOfExp"),data.get("degree"),data.get("passout"),data.get("college"))
 
    dic ={"message":message}
    return jsonify(dic  ) 




@app.route("/getdata", methods=['POST'])
def retrive_features():
    data= request.json
    
    name,phoneNo,email,jobTitle,organization,yearsOfExp,degree,passOutYear,college = retrive_all(data.get("phoneNo")) 


    dict ={"name":name,"phoneNo":phoneNo,"email":email,"jobTitle":jobTitle,"oraganization":organization,"yearsOfExp":yearsOfExp,"degree":degree,"passOutYear":passOutYear,"college":college}
    
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