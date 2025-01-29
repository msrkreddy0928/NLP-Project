import pdf_text_extraction
from pdf_text_extraction import extract_text_from_pdf
from preprocessing import text_to_words,split_lines
from feature_extraction import phone_num_extrcat,name_extract,experience_extract,education_extract,pass_out_year_extract,degree_extraction,college_extraction,extract_summary
from mysqldb import insert,retrive

def pipeline(path):
   
   text = extract_text_from_pdf(path)

   words = text_to_words(text)
   
   lines = split_lines(text)
   
   phone_num =  phone_num_extrcat(text)      
  
   exp=experience_extract(lines)
   
   name = name_extract(text)
         
   education = education_extract(lines)
   
   degree= degree_extraction(education)
   
   college,degree_1 =college_extraction(lines)
   
   passout = pass_out_year_extract(lines)
   
   summary=extract_summary(lines,name,phone_num)
   
   
   if degree_1 != "":
      degree=degree_1

   if degree=='' and degree_1=='':
      degree="Degree not found"
   
   if exp ==None:
      exp = "Experience not found"
      
   if college =='':
      college="College not found"   
      
    
   print(name)
   print(phone_num)
   print(passout)
   print(degree)
   print(college)
   print(exp)
   print(summary)
        
    

      
   # sno = insert(name,phone_num,passout,degree,college,exp)
   
   # sno,name,phoneNo,passOutYear,degree,college,yearsOfExp = retrive(sno)

   
   return name,phone_num,degree,passout,college,exp
   
   


path0 = "/home/shiva/Downloads/resumes/Untitled design.pdf"

path1 = "/home/shiva/Downloads/resumes/London-Resume-Template-Professional.pdf" 

path2 = "/home/shiva/Downloads/resumes/Abhishek Gunda.pdf"

path3 = "/home/shiva/Downloads/resumes/Azhar khan.pdf" 

path4 = "/home/shiva/Downloads/resumes/Dhananjay Kumar Yadav.pdf" 

path5 = "/home/shiva/Downloads/resumes/Ketan Gwari.pdf"

path6 = "/home/shiva/Downloads/resumes/Nanneboina Ramana.pdf"

path7 = "/home/shiva/Downloads/resumes/Shaik Luqman.pdf"

path8 = "/home/shiva/Downloads/resumes/Swpana Kumari Sahu.pdf"

path9 = "/home/shiva/Downloads/resumes/Kashetti_Venu.pdf"

path10 = "/home/shiva/Downloads/resumes/Dublin-Resume-Template-Modern.pdf"

path11 = "/home/shiva/Downloads/resumes/Sydney-Resume-Template-Modern.pdf"

path12 = "/home/shiva/Downloads/resumes/Vienna-Modern-Resume-Template.pdf"



if __name__== '__main__':  
   pipeline(path4)      