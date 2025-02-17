from flask import Flask,render_template,request,json,jsonify,send_file
import requests
import pdfplumber
import os
import sys
sys.path.append('/home/shiva/Desktop/ML/Resume Parser/NLP-Project/src')
from src.pipelines import pipeline_start
from src.mysqldb import insert_all,retrieve_all,retrieve_resumes
from src.feature_extraction import add_title,add_skills,add_skills_from_matcher
from flask_cors import CORS
import io
from src.matching import skill_matcher,job_description_matcher


app = Flask(__name__)


CORS(app)

file_data =None
file = None
file_path = None



# Route for the home page
@app.route("/")
def home():
   
    return render_template('home.html')


@app.route("/jobmatcher")
def job_matcher_home():
    
    return render_template('match.html')


# Route for feature extraction from the uploaded resume
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
    
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percentage2,pl,fs,bs,ds,oss,org_list,exp_list = pipeline_start(file_data)
    
    
    
    if degree1 is None:
        degree1=degree2
        passOutYear1=passOutYear2
        college1=college2
        degree2=None
        passOutYear2=None
        college2=None 
     
    percentage1=None
    percentage2 = None
 
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"certifications":certifications,"projects":projects,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":oss,"org":org_list,"exp":exp_list}
    
    return jsonify(dict), 200 


@app.route("/extractdetails",methods=['POST'])
def feature_extractions():
    

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
    
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,college1,passOutYear1,skills = pipeline_start(file_data)
    
    
    
    # if degree1 is None:
    #     degree1=degree2
    #     passOutYear1=passOutYear2     
    #     college1=college2
    #     degree2=None
    #     passOutYear2=None
    #     college2=None 
     
    # percentage1=None
    # percentage2 = None
 
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"Highestdegree":degree1,"college":college1,"passOutYear":passOutYear1,"skills":skills}
    
    return jsonify(dict), 200  


@app.route("/extractdetails1")
def feature_extractions1():

    # if 'file' not in request.files:
    #     return "No file part", 400
    
    file_url = request.args.get('file_url') 

   
    
    if not file_url:
        return "No file URL provided", 400
    
    try:
        response = requests.get(file_url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        return f"Error downloading file: {e}", 400 
    

    try:
        file_data = io.BytesIO(response.content)
    
        name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,college1,passOutYear1,skills = pipeline_start(file_data)
    
 
        dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"Highestdegree":degree1,"college1":college1,"passOutYear":passOutYear1,"skills":skills}
    
    except:
        return "Error occured while extracting data"
    

    return jsonify(dict), 200  



 
 # Route for saving extracted features to the database    
@app.route("/save", methods=['POST'])
def save_features():
    data= request.json
    
    print(data)
    
    job_title=data.get("jobTitle")
    
    add_title(job_title)
    
    dict1={}
    
    dict1["programming_languages"] = data.get('pl').split(",")
   
    dict1["frontend_skills"] = data.get('fs').split(",")
    
    dict1['backend_skills'] = data.get('bs').split(",")
    
    dict1["databases"] = data.get('ds').split(",")
    
    dict1["other_skills"] = data.get('os').split(",")
    
    add_skills(dict1)
    
    
    list1=[]
    
    if file_data!=None and file!=None:
        file_data.seek(0)
        list1.append(file_data)
        list1.append(file)
        
    else:
        list1.append(file_path)
  
    org =','.join(data.get("org"))
    exp = ','.join(data.get("exp"))     

    message = insert_all(data.get("name"),data.get("phoneNo"),data.get("countryCode"),data.get("email"),data.get("jobTitle"),data.get("organization"),data.get("yearsOfExp"),data.get("degree1"),data.get("degree2"),data.get("passOutYear1"),data.get("passOutYear2"),data.get("college1"),data.get("College2"),data.get("summary"),data.get("certifications"),data.get("projects"),data.get("percentage1"),data.get("percenatge2"),data.get("pl"),data.get("fs"),data.get("bs"),data.get("ds"),data.get("os"),org,exp,list1)
     
     
    dic ={"message":message}
    return jsonify(dic) 



# Route to retrieve extracted features based on phone number
@app.route("/getdata", methods=['POST'])
def retrieve_features():
    data= request.json
    
    print(data.get("phoneNo"))
    
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percentage2,pl,fs,bs,ds,os,org,exp= retrieve_all(data.get("phoneNo")) 
 
    
    dict ={"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"certifications":certifications,"projects":projects,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":os,"org":org.split(","),"exp":exp.split(",")}
    
    return jsonify(dict)



# Route to retrieve resumes from the database and prepare for download
@app.route("/getdetails",methods =['post'])
def retrieve_resumes_from_db():
    data = request.json
    
    file_name,file_data = retrieve_resumes(data.get("phoneNo"))
    
    
    download_path = os.path.join("/home/shiva/Downloads/resumesStore",file_name)

    with open(download_path, 'wb') as file:
            file.write(file_data)   
    
    global file_path
    file_path=download_path
    name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percentage2,pl,fs,bs,ds,oss,org_list,exp_list = pipeline_start(download_path)
    
    
    
    if degree1 is None:
        degree1=degree2
        passOutYear1=passOutYear2
        college1=college2
        degree2=None
        passOutYear2=None
        college2=None 
     
    percentage1=None
    percentage2 = None
    
 
    dict ={"file":download_path,"name":name,"phoneNo":phoneNo,"countryCode":countryCode,"email":email,"jobTitle":jobTitle,"organization":organization,"yearsOfExp":yearsOfExp,"degree1":degree1,"degree2":degree2,"college1":college1,"college2":college2,"passOutYear1":passOutYear1,"passOutYear2":passOutYear2,"summary":summary,"certifications":certifications,"projects":projects,"percentage1":percenatge1,"percentage2":percentage2,"pl":pl,"fs":fs,"bs":bs,"ds":ds,"os":oss,"org":org_list,"exp":exp_list}
    
    return jsonify(dict), 200 
  


# Route to download the resume file
@app.route('/download')
def download_file():
    
    return send_file(file_path)



 
 # Route to match skills with existing skills in the database 
@app.route("/match",methods=['POST'])
def match_skills():
    
    data = request.json
    
    skills = data.get("skills")

    
    add_skills_from_matcher(skills.split(","))
    
    dict1 = skill_matcher(data.get("skills"))
    
    return jsonify(dict1),200  


 # Route to match job descriptions 
@app.route("/matchdesc",methods=['POST'])
def match_desc():
    
    data = request.json
    
    dict1 = job_description_matcher(data.get("desc"))
    
    return jsonify(dict1),200  

  
  
# Start the Flask app 

if __name__=="__main__":
   app.run(host='192.168.10.130', port=5000)