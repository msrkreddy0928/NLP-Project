from flask import Flask,render_template,request,json,jsonify,send_file
import requests
import pdfplumber
import os
import sys
sys.path.append('/home/shiva/Desktop/ML/Files/NLP/src')
from src.pipelines import pipeline_start
from src.mysqldb import update,insert_all,retrieve_all,retrieve_resumes
from src.feature_extraction import add_title
from flask_cors import CORS
import io
from src.matching import skill_matcher


app = Flask(__name__)


CORS(app)

file_data =None
file = None
file_path = None

@app.route("/")
def home():
   
    return render_template('match.html')


@app.route("/extract",methods=['POST'])
def feature_extraction():
    

    if 'file' not in request.files:
        return "No file part", 400
    
    doc = request.files['file']

    
    global file
    file=doc
    
    global file_data
    file_data = io.BytesIO(doc.read())
    
    if  doc.filename == '':
        return "No selected file", 400
    
    file_data.seek(0)
    
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percentage2,pl,fs,bs,ds,oss = pipeline_start(file_data)
    
    
    
    if degree1 is None:
        degree1=degree2
        passOutYear1=passOutYear2
        college1=college2
        degree2=None
        passOutYear2=None
        college2=None 
     
    percentage1=None
    percentage2 = None
 
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"certifications":certifications,"projects":projects,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":oss}
    
    return jsonify(dict), 200 
    
 
 
     
@app.route("/save", methods=['POST'])
def save_features():
    data= request.json
    
    print(data)
    
    job_title=data.get("jobTitle")
    
    add_title(job_title)
    
    if file_data!=None:
        file_data.seek(0)
        
    
    resume = download_file()
    print("resume",resume)    

    message = insert_all(data.get("name"),data.get("phoneNo"),data.get("countryCode"),data.get("email"),data.get("jobTitle"),data.get("organization"),data.get("yearsOfExp"),data.get("degree1"),data.get("degree2"),data.get("passOutYear1"),data.get("passOutYear2"),data.get("college1"),data.get("College2"),data.get("summary"),data.get("certifications"),data.get("projects"),data.get("percentage1"),data.get("percenatge2"),data.get("pl"),data.get("fs"),data.get("bs"),data.get("ds"),data.get("os"),file_data,file)
     
     
    dic ={"message":message}
    return jsonify(dic) 




@app.route("/getdata", methods=['POST'])
def retrieve_features():
    data= request.json
    
    print(data.get("phoneNo"))
    
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percentage2,pl,fs,bs,ds,os= retrieve_all(data.get("phoneNo")) 
 
    
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"certifications":certifications,"projects":projects,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":os}
    
    return jsonify(dict)


@app.route("/getdetails",methods =['post'])
def retrieve_resumes_from_db():
    data = request.json
    
    file_name,file_data = retrieve_resumes(data.get("phoneNo"))
    
    download_path = os.path.join("/home/shiva/Downloads/resumesStore",file_name)

    with open(download_path, 'wb') as file:
            file.write(file_data)   
    
    global file_path
    file_path=download_path
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percentage2,pl,fs,bs,ds,oss = pipeline_start(download_path)
    
    
    
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
 
    dict ={"file":download_path,"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"certifications":certifications,"projects":projects,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":oss}
    
    return jsonify(dict), 200 
  


@app.route('/download')
def download_file():
    
    return send_file(file_path)



@app.route("/save",methods=['POST'])
def save_modify_features():
    
    rows_aff = None
    data = request.get_json()
    sno_=0
    rows_aff=update(sno_,data)
    
    print(rows_aff)
    
    return "ok"
  
  
@app.route("/match",methods=['POST'])
def match_skills():
    
    data = request.json
    
    dict1 = skill_matcher(data.get("skills"))
    
    return jsonify(dict1),200  
  
  
    

if __name__=="__main__":
   app.run(host='192.168.10.130', port=5000)