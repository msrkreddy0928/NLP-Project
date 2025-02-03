import pdf_text_extraction
from pdf_text_extraction import extract_text_from_pdf,extract_text
from preprocessing import text_to_words,split_lines,line_remover
from feature_extraction import extract_phone_num,extract_name,extrcat_experience,extract_education,pass_out_year_extract,extract_degree,extract_college,extract_summary,extract_education_1,extract_passout,extract_education_text,extract_college_1,extract_degree_1,extract_summary_1,extract_experience_1,extract_percentage
# from mysqldb import insert,retrive
from transformers import pipeline    


def pipeline_start(path):
   

   model =pipeline("text2text-generation",model="google/flan-t5-large")
   
   text,text_list  = extract_text(path)

   # print(text_list)
   
   text_list = line_remover(text_list)
   
   # lines = text.splitlines()

   education_lines = extract_education_text(text_list)
   
   print("Edu",education_lines[:7])
                          
   education_text_=""
   for line in education_lines[:7]:
      education_text_=education_text_+" "+line
      
   degrees_dict_1= extract_degree_1(education_text_)
   
   degree1=None
   degree2=None
   
   degree1 = degrees_dict_1["pg"]

   degree2 = degrees_dict_1["grad"]

   print("dict",degrees_dict_1)
   
   if degree1 is not None or degree2 is not None:
      
      print("hello")
    
      name = extract_name(text[:400],model)
      
      phone_num,countryCode =  extract_phone_num(text)
      
      colleges = extract_college(education_lines,model,degree1,degree2)
      
      summary=extract_summary_1(text)
      
      exp = extract_experience_1(summary)
      
      # percentage =
      extract_percentage(education_text_)
      
      college1,college2,pass_out_year_1,pass_out_year_2 = extract_college_1(education_text_,degree1,degree2)

 
   
   else:
      
      text = extract_text_from_pdf(path)
      
      words = text_to_words(text)
      
      lines = split_lines(text)
      
      name = extract_name(text,model)
      
      phone_num,countryCode =  extract_phone_num(text)
      
      exp = extrcat_experience(lines)
         
      pass_out_year_1 = pass_out_year_extract(lines)
   
      summary=extract_summary(lines,name,phone_num)
      
      education_text = extract_education_text(lines)
      
      degrees = extract_education_1(education_text,model)
      
      education = extract_education(education_text,model)
      
      extract_percentage(education_text)
      
      degrees_dict_1= extract_degree(degrees)
      
      degrees_dict_2 = extract_degree(education)
      
      if degrees_dict_1["grad"] is None:
         
         if degrees_dict_2["grad"] is not None:
            degree2 = degrees_dict_2["grad"]
         else:
            degree2 = None
      else:
         degree2=degrees_dict_1["grad"]
      
           
      college1,college2,degree_= extract_college(lines,model,degree1,degree2)
      
    
      if degree1 is None:
         degree1=degree_["pg"]
   
      elif degree2 is None:
         degree2=degree_["grad"]   
   
   

      extract_passout(degrees,degree1,degree2)
   
      if exp ==None:
         exp = "Experience not found"
      
      if college1 =='':
         college1="College not found"   
         
      if college2 == None:
         college = "COllege not found"
   

 
    
   

 
 
 
   print("name",name)
   print("phoneNO",phone_num)
   print("countryCode",countryCode)
   print("degree1",degree1)
   print("degree2",degree2)
   print("college1",college1)
   print("college2",college2)
   print("pass_out_year_1",pass_out_year_1)
   print("pass_out_year_2",pass_out_year_2)
   print(exp)
   print("summary",summary)
        
      
   # sno = insert(name,phone_num,passout,degree,college,exp)
   
   # sno,name,phoneNo,passOutYear,degree,college,yearsOfExp = retrive(sno)

   
   return name,phone_num,countryCode,degree1,degree2,pass_out_year_1,pass_out_year_2,college1,college2,exp,summary
   
   


path0 = "/home/shiva/Downloads/resumes/Untitled design.pdf"

path1 = "/home/shiva/Downloads/resumes/London-Resume-Template-Professional.pdf" 

path2 = "/home/shiva/Downloads/resumes/Azhar khan.pdf"

path3 = "/home/shiva/Downloads/resumes/Abhishek Gunda.pdf"

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

path14 ="/home/shiva/Downloads/resumes/Resume_Madhuri-1 1.pdf"

if __name__== '__main__':  
   pipeline_start(path4)