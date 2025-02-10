from pdf_text_extraction import extract_text_from_pdf,extract_text
from feature_extraction import extract_phone_num
from mysqldb import save_resumes,retrieve_resumes
import os
from pipelines import pipeline_start




#saves the resumes to the database.
def save_resumes_to_db(path):
    
    text_plumber = extract_text_from_pdf(path)
  
    phone_num,countryCode =  extract_phone_num(text_plumber)

    save_resumes(path,phone_num)






# retrieves the resumes from the database.

def retrive_resumes_from_db(phoneNo):
    file_name,file_data = retrieve_resumes(phoneNo)
    
    download_path = os.path.join("/home/shiva/Downloads/resumesStore", file_name)
    
    with open(download_path, 'wb') as file:
             file.write(file_data)   
            
            

  
            
