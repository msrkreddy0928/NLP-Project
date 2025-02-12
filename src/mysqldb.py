from config import db_connection
import io
import mimetypes



#Inserts resume data into the parser table if the candidate doesn't already exist in the database.
def insert_all(name,phoneNo,countryCode,email,jobTitle,organization,expYears,degree1,degree2,passOutYear1,passOutYear2,college1,college2,summary,certifications,projects,percentage1,percentage2,pl,fs,bs,ds,os,org,exp,list1):
    
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
            query = "INSERT INTO parser(name,phoneNo,countryCode,email,jobTitle,organization,expYears,degree1,degree2,passOutYear1,passOutYear2,college1,college2,summary,percentage1,percentage2,pl,fs,bs,ds,os,certifications,projects,allOrg,allExp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (name,phoneNo,countryCode,email,jobTitle,organization,expYears,degree1,degree2,passOutYear1,passOutYear2,college1,college2,summary,percentage1,percentage2,pl,fs,bs,ds,os,certifications,projects,org,exp)
            cursor.execute(query,values)
            mydb.commit()
        
            query = "select sno from parser where phoneNo=%s"
            cursor.execute(query,(phoneNo,))
            sno = cursor.fetchone()
            print(sno[0])
            if len(list1)==1:
                insert_doc_from_path(list1[0],sno[0])
            else:
                insert_doc(list1[0],list1[1],sno[0])    
        
        except:
             mydb.rollback()
             
             return "Error in saving data"
              
        finally:
             cursor.close()
             mydb.close()
    
        return "Data saved successfully"
    
    
    
#Inserts a resume file into the pdf_files table using binary data and file type information.   
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
         



#Inserts a resume file from a given file path into the pdf_files table.
def insert_doc_from_path(file,sno):
    mydb = db_connection()
    cursor = mydb.cursor()
    file_name = file.split('/')[-1]
    
    mime_type, encoding = mimetypes.guess_type(file)
    
    with open(file,"rb") as file:
        binary_data = file.read()
             
    query = "INSERT INTO pdf_files (filename, file_data,file_type,parserSno)VALUES (%s, %s, %s,%s)"
    values = (file_name,binary_data,mime_type,sno)
    cursor.execute(query,values)
    mydb.commit()
    
    cursor.close()
    mydb.close()
 
 
    
#Retrieves all features associated with a specific candidate based on their phone number.
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
    org = feature_list[0][24]
    exp = feature_list[0][25]
    
    
    return name,phoneNo,countryCode,email,jobTitle,organization,yearsOfExp,degree1,degree2,college1,college2,passOutYear1,passOutYear2,summary,certifications,projects,percenatge1,percenatge2,pl,fs,bs,ds,os,org,exp




#Retrieves a list of candidates based on a custom query from the database.
def retrieve_all_candidates(query):
    
    mydb = db_connection()
    cursor = mydb.cursor()

    cursor.execute(query)
    feature_list = cursor.fetchall()
    
    # print(feature_list)

    return feature_list




    
#Saves a resume file into the resume_files table by storing the binary data along with content type.
    
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
    
 
 
#Retrieves a resume's filename and binary file data for a given phone number from resume_files table. 
def retrieve_resumes(phoneNo):
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    query = "select filename,file_data from resume_files where phoneno=%s"
    values = (phoneNo,)
    cursor.execute(query,values)
    result = cursor.fetchone()
    
    return result[0],result[1]
    


    
    
    

  
  
    
    
    

    

    
    
    
    
    