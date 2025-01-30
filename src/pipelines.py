import pdf_text_extraction
from pdf_text_extraction import extract_text_from_pdf
from preprocessing import text_to_words,split_lines
from feature_extraction import phone_num_extrcat,name_extract,experience_extract,education_extract,pass_out_year_extract,degree_extraction,college_extraction,extract_summary,extract_degree2
from mysqldb import insert,retrive
from transformers import pipeline    


def pipeline_start(path):
   
   
   model =pipeline("text2text-generation",model="google/flan-t5-large")
   
   
   text = extract_text_from_pdf(path)

   words = text_to_words(text)
   
   lines = split_lines(text)
   
   phone_num =  phone_num_extrcat(text)      
  
   
   name = name_extract(text,model)
   
   exp=experience_extract(lines)
   
   degrees = extract_degree2(lines,model)
         
   education = education_extract(lines,model)
   
   degrees_dict_1= degree_extraction(degrees)
   degrees_dict_2 = degree_extraction(education)
   
   if degrees_dict_1["pg"] is None:
      if degrees_dict_2["pg"] is not None:
         degree1=degrees_dict_2["pg"]
      else:
         degree1 = None
   
   else:
      degree1=degrees_dict_1['pg']
      
   
   if degrees_dict_1["grad"] is None:
      if degrees_dict_2["grad"] is not None:
         degree2 = degrees_dict_2["grad"]
      else:
         degree2 = None
   else:
      degree2=degrees_dict_1["grad"]
      
      
   college1,college2,degree_ =college_extraction(lines,model,degree1,degree2)
   
   if degree1 is None:
      degree1=degree_["pg"]
   
   elif degree2 is None:
      degree2=degree_["grad"]   
   
   passout = pass_out_year_extract(lines)
   
   summary=extract_summary(lines,name,phone_num)

   
   
   if exp ==None:
      exp = "Experience not found"
      
   if college1 =='':
      college1="College not found"   
 
 
   if college2 == None:
      college = "COllege not found"
 
 
 
   print(name)
   print(phone_num)
   print(passout)
   print(degree1)
   print(degree2)
   print(college1)
   print(college2)
   print(exp)
   print(summary)
        
      
   # sno = insert(name,phone_num,passout,degree,college,exp)
   
   # sno,name,phoneNo,passOutYear,degree,college,yearsOfExp = retrive(sno)

   
   return name,phone_num,degree1,degree2,passout,college1,college2,exp,summary
   
   


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

path13 = "/home/shiva/Downloads/resumes/New-York-Resume-Template-Creative.pdf"



if __name__== '__main__':  
   pipeline_start(path2)      