from pdf_text_extraction import extract_text_from_pdf,extract_text
from feature_extraction import extract_phone_num
from mysqldb import save_resumes,retrieve_resumes
import os
from pipelines import pipeline_start

path ="/home/shiva/Downloads/resumes/Dhananjay Kumar Yadav.pdf"

path2 = "/home/shiva/Downloads/resumes/Azhar khan.pdf"

path3 = "/home/shiva/Downloads/resumes/Abhishek Gunda.pdf"

 

path5 = "/home/shiva/Downloads/resumes/Ketan Gwari.pdf"

path6 = "/home/shiva/Downloads/resumes/Nanneboina Ramana.pdf"

path7 = "/home/shiva/Downloads/resumes/Shaik Luqman.pdf"

path8 = "/home/shiva/Downloads/resumes/Swpana Kumari Sahu.pdf"

path9 = "/home/shiva/Downloads/resumes/Kashetti_Venu.pdf"
path16  = "/home/shiva/Downloads/resumes/Nangi Ramesh.pdf"

path17 = "/home/shiva/Downloads/resumes/Venkata Reddy Yeruva.pdf"



#saves the resumes to the database.
def save_resumes_to_db(path):
    
    text_plumber = extract_text_from_pdf(path)
  
    phone_num,countryCode =  extract_phone_num(text_plumber)

    save_resumes(path,phone_num)


save_resumes_to_db(path17)

# file_name,file_data = retrieve_resumes(phone_num)



# download_path = os.path.join("/home/shiva/Downloads/resumesStore", file_name)

# with open(download_path, 'wb') as file:
#             file.write(file_data)   
            
            

  
            
