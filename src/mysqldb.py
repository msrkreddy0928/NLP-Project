from config import db_connection




def insert_all(name,phoneNo,email,jobTitle,organization,expYears,degree,passOutYear,college):
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    query1 = "select * from parser where phoneNo=%s"
    
    values =(phoneNo,)

    
    cursor.execute(query1,values)
    
    data = cursor.fetchall()
    
    if len(data)>0:
        return "Candidate already exist in the database"
    
    else:
        query = "INSERT INTO parser(name,phoneNo,email,jobTitle,organization,expYears,degree,passOutYear,college) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (name,phoneNo,email,jobTitle,organization,expYears,degree,passOutYear,college)
        cursor.execute(query,values)
        mydb.commit()
        
        return "Data saved successfully"
    
    
def retrive_all(phoneNo):  
    mydb = db_connection()
    cursor = mydb.cursor()
    query = "select * from parser where phoneNo="+phoneNo
    cursor.execute(query)
    feature_list = cursor.fetchall()
    
    print(feature_list)

    sno = feature_list[0][0]
    name=feature_list[0][1]
    phoneNo=feature_list[0][2]
    email=feature_list[0][3]
    jobTitle=feature_list[0][4]
    organization=feature_list[0][5]
    yearsOfExp=feature_list[0][6]
    degree=feature_list[0][7]
    passOutYear=feature_list[0][8]
    college=feature_list[0][9]
   
    
    return name,phoneNo,email,jobTitle,organization,yearsOfExp,degree,passOutYear,college    




def insert(name,phoneNo,passOutYear,degree,college,yearsOfExp):
    
    mydb = db_connection()
    cursor = mydb.cursor()
    
    query = "INSERT INTO resume(name,phoneNo,passOutYear,degree,college,yearsOfExp) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (name,phoneNo,passOutYear,degree,college,yearsOfExp)
    cursor.execute(query,values)
    mydb.commit()
    query = "select sno from resume where phoneNo=%s"
    cursor.execute(query,(phoneNo,))
    sno=cursor.fetchone()
    mydb.close()
    if sno[0]:
        return sno[0]
    else:
        return None
      
    
def retrive(sno):  
    mydb = db_connection()
    cursor = mydb.cursor()
    query = "select * from resume where sno="+str(sno)
    cursor.execute(query)
    feature_list = cursor.fetchall()
    sno = feature_list[0][0]
    name=feature_list[0][1]
    phoneNo=feature_list[0][2]
    passOutYear=feature_list[0][3]
    degree=feature_list[0][4]
    college=feature_list[0][5]
    yearsOfExp=feature_list[0][6]
    
    return sno,name,phoneNo,passOutYear,degree,college,yearsOfExp
    
def update(sno,dict):
  
  mydb = db_connection()
  cursor = mydb.cursor()  
  query=   "UPDATE resume SET name = %s, phoneNo = %s, passOutYear = %s, degree = %s, college = %s, yearsOfExp =%s WHERE sno = %s"
  values = (dict['name'],dict['phoneNo'],dict['passOutYear'],dict['degree'],dict['college'],dict['expYears'],sno)
  rows_aff = cursor.execute(query,values)
  mydb.commit()
  
  return rows_aff
  
  
    
    
    

    

    
    
    
    
    