from config import db_connection
import io
import mimetypes


def insert_all(name,phoneNo,countryCode,email,jobTitle,organization,expYears,degree1,degree2,passOutYear1,passOutYear2,college1,college2,summary,certifications,projects,percentage1,percentage2,pl,fs,bs,ds,os,file_data,file):
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    query1 = "select * from parser where phoneNo=%s"
    
    values =(phoneNo,)

    
    cursor.execute(query1,values)
    
    data = cursor.fetchall()
    
    if len(data)>0:
        return "Candidate already exist in the database"
    
    else:
        try:
            query = "INSERT INTO parser(name,phoneNo,countryCode,email,jobTitle,organization,expYears,degree1,degree2,passOutYear1,passOutYear2,college1,college2,summary,percentage1,percentage2,pl,fs,bs,ds,os,certifications,projects) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (name,phoneNo,countryCode,email,jobTitle,organization,expYears,degree1,degree2,passOutYear1,passOutYear2,college1,college2,summary,percentage1,percentage2,pl,fs,bs,ds,os,certifications,projects)
            cursor.execute(query,values)
            mydb.commit()
        
            query = "select sno from parser where phoneNo=%s"
            cursor.execute(query,(phoneNo,))
            sno = cursor.fetchone()
            print(sno[0])
            insert_doc(file_data,file,sno[0])
        
        except:
             mydb.rollback()
             
             return "Error in saving data"
              
        finally:
             cursor.close()
             mydb.close()
    
        return "Data saved successfully"
    
    
    
    
def insert_doc(file_data,file,sno):
    mydb = db_connection()
    cursor = mydb.cursor()
     
    binary_data = file_data.read()
      
    query = "INSERT INTO pdf_files (filename, file_data,file_type,parserSno)VALUES (%s, %s, %s,%s)"
    values = (file.filename,binary_data,file.content_type,sno)
    cursor.execute(query,values)
    mydb.commit()
    
    cursor.close()
    mydb.close()
         
 
 
 
    
    
def retrieve_all(phoneNo):  
    mydb = db_connection()
    cursor = mydb.cursor()
    query = "select * from parser where phoneNo=%s"
    values =(phoneNo,)
    cursor.execute(query,values)
    feature_list = cursor.fetchall()
    # if len(feature_list)==0:
    #     return "candidate not found"
    
    
    print(feature_list)

    # sno = feature_list[0][0]
    name=feature_list[0][1]
    phoneNo=feature_list[0][2]
    email=feature_list[0][3]
    jobTitle=feature_list[0][4]
    organization=feature_list[0][5]
    yearsOfExp=feature_list[0][6]
    degree1=feature_list[0][7]
    passOutYear1 = feature_list[0][8]
    college1 = feature_list[0][9]
    degree2 = feature_list[0][10]
    college2 = feature_list[0][11]
    passOutYear2=feature_list[0][12]
    countryCode = feature_list[0][13]
    summary=feature_list[0][14]
    percenatge1=feature_list[0][15]
    percenatge2 =feature_list[0][16]
    pl=feature_list[0][17]
    fs=feature_list[0][18]
    bs=feature_list[0][19]
    ds=feature_list[0][20]
    os= feature_list[0][21]
    certifications=feature_list[0][22]
    projects = feature_list[0][23]
    
    
    return name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percenatge2,pl,fs,bs,ds,os



def retrieve_all_candidates():
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    query = "select name,email,phoneNo,pl,fs,bs,ds,os from parser"
    
    cursor.execute(query)
    feature_list = cursor.fetchall()
    
    # print(feature_list)

    return feature_list



retrieve_all_candidates()
    
    
    
def save_resumes(file,phoneNo):
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    file_name = file.split('/')[-1]
    
    mime_type, encoding = mimetypes.guess_type(file)
    
    with open(file,'rb') as file:
        binary_data = file.read()
      
    query = "INSERT INTO resume_files(phoneno,filename,file_data,file_type)VALUES (%s, %s, %s,%s)"
    values = (phoneNo,file_name,binary_data,mime_type)
    cursor.execute(query,values)
    mydb.commit()
    
    cursor.close()
    mydb.close()
    
    
def retrieve_resumes(phoneNo):
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    query = "select filename,file_data from resume_files where phoneno=%s"
    values = (phoneNo,)
    cursor.execute(query,values)
    result = cursor.fetchone()
    
    return result[0],result[1]
    


    

    
    
    
def update(sno,dict):
  
  mydb = db_connection()
  cursor = mydb.cursor()  
  query=   "UPDATE resume SET name = %s, phoneNo = %s, passOutYear = %s, degree = %s, college = %s, yearsOfExp =%s WHERE sno = %s"
  values = (dict['name'],dict['phoneNo'],dict['passOutYear'],dict['degree'],dict['college'],dict['expYears'],sno)
  rows_aff = cursor.execute(query,values)
  mydb.commit()
  
  return rows_aff
  
  
    
    
    

    

    
    
    
    
    