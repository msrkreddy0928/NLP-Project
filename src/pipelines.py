import pdf_text_extraction
from pdf_text_extraction import extract_text_from_pdf,extract_text
from preprocessing import text_to_words,split_lines,line_remover
from feature_extraction import extract_phone_num,extract_name,extract_experience,extract_education,pass_out_year_extract,extract_degree,extract_college,extract_summary,extract_education_1,extract_passout,extract_education_text,extract_passout_1,extract_degree_1,extract_summary_1,extract_experience_1,extract_percentage,extract_certifications,extract_college_1,extract_email,extract_title,extract_latest_organization,extract_skills,extract_projects
# from mysqldb import insert,retrive
from transformers import pipeline    


from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]


def pipeline_start(path):
   

   model =pipeline("text2text-generation",model="google/flan-t5-large")
   
   text_pymu,text_list_pymu  = extract_text(path)
   
   # print(text_pymu[:700])
   
   text_plumber = extract_text_from_pdf(path)
      
   lines_plumber = split_lines(text_plumber)

   # print(text_list)
   
   text_list_pymu = line_remover(text_list_pymu)
   
   # lines = text.splitlines()
   
   education_lines = extract_education_text(text_list_pymu)

   
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
   
   name = extract_name(text_plumber,model)
   
   email = extract_email(text_plumber)
   
   if degree1 is not None or degree2 is not None:
      
      print("hello")
    
      # name = extract_name(text_pymu[:700],model)
      
      phone_num,countryCode =  extract_phone_num(text_pymu)
      
      colleges = extract_college(education_lines,model,degree1,degree2)
      
      summary=extract_summary_1(text_pymu)
      
      exp = extract_experience_1(summary)
      
      if exp is None:
         exp = extract_experience(lines_plumber)
      
      # extract_percentage(education_text_)
      
      certifications = extract_certifications(text_list_pymu)
      
      projects = extract_projects(text_list_pymu)
      
      college11,college22 =  extract_college_1(education_lines,model,degree1,degree2)
      
      college1,college2,degree_= extract_college(lines_plumber,model,degree1,degree2)
      
      if college1.lower()=="education":
         college1=college11
      if college2.lower()=="education":
         college2=college22   
      
      if degree1 is None and degree2 is not None:
         college2=college1
         college1=None
      
      if degree2 is None:
         college2 =None   
      
      
      
      pass_out_year_1,pass_out_year_2 = extract_passout_1(education_text_,degree1,degree2)
      
      if degree1 is not None:
         if degree1.split()[0].lower() in ["m.","post"]:
                degree1 = ''.join(degree1.split()[:2])
              
         else:
            degree1=degree1.split()[0]
      
      if degree2 is not None:
         if degree2.split()[0].lower() in ["b.","under"]:
                degree2 = ''.join(degree2.split()[:2])
         else:
            degree2= degree2.split()[0]
         
      
   else:
 
   
      
      phone_num,countryCode =  extract_phone_num(text_plumber)
      
      exp = extract_experience(lines_plumber)
         
      pass_out_year_1 = pass_out_year_extract(lines_plumber)

   
      summary=extract_summary(lines_plumber,name,phone_num)
      
      education_text = extract_education_text(lines_plumber)
      
      degrees = extract_education_1(education_text,model)
      
      education = extract_education(education_text,model)
      
      
      # extract_percentage(education_text)
      
      degrees_dict_1= extract_degree(degrees)
      
      degrees_dict_2 = extract_degree(education)
      
      
      if degrees_dict_1["pg"] is None:
         
         if degrees_dict_2["pg"] is not None:
            degree1 = degrees_dict_2["pg"]
         else:
            degree1 = None
      else:
         degree1=degrees_dict_1["pg"]
         
         
         
     
      if degrees_dict_1["grad"] is None:
         
         if degrees_dict_2["grad"] is not None:
            degree2 = degrees_dict_2["grad"]
         else:
            degree2 = None
      else:
         degree2=degrees_dict_1["grad"]
         
           
      college1,college2,degree_= extract_college(lines_plumber,model,degree1,degree2)
      
      
      if degree1 is None and degree2 is not None:
         college2=college1
         college1=None
      
      if degree2 is None:
         college2 =None 
      
      # certifications = extract_certifications(lines_plumber) 
       
     
      if degree1 is None:
         degree1=degree_["pg"]
   
      elif degree2 is None:
         degree2=degree_["grad"]   
   
      
      
      pass_out_year_2 = extract_passout(degrees,degree1,degree2)
      
      certifications = extract_certifications(lines_plumber)
      
      projects = extract_projects(lines_plumber)
     
   
      if exp ==None:
         exp = "Experience not found"
      
      if college1 =='':
         college1="College not found"   
         
      if college2 == None:
         college = "COllege not found"
   

 
    
   
   title =  extract_title(text_plumber,model)
      
   latest_organization = extract_latest_organization(text_plumber,model)
      
   skills = extract_skills(text_plumber)
      
 
 
   print("name",name)
   print("phoneNO",phone_num)
   print("email",email)
   print("countryCode",countryCode)
   print("degree1",degree1)
   print("degree2",degree2)
   print("college1",college1)
   print("college2",college2)
   print("pass_out_year_1",pass_out_year_1)
   print("pass_out_year_2",pass_out_year_2)
   print("EXP",exp)
   print("title",title)
   print("latest_org",latest_organization)
   print("skills",skills)
   print("summary",summary)
   print("certifications",certifications)
   print("projects",projects)
        
      
   # sno = insert(name,phone_num,passout,degree,college,exp)
   
   # sno,name,phoneNo,passOutYear,degree,college,yearsOfExp = retrive(sno)
   percentage1 = None
   percentage2 = None
   
   return name,phone_num,countryCode,email,title,latest_organization,exp,degree1,degree2,college1,college2,pass_out_year_1,pass_out_year_2,summary,certifications,projects,percentage1,percentage2,skills['programming_languages'],skills['frontend_skills'],skills['backend_skills'],skills['databases'],skills['other_skills']
   
   


path0 = "/home/shiva/Downloads/resumes/Untitled design.pdf"

path1 = "/home/shiva/Downloads/resumes/London-Resume-Template-Professional.pdf" 

path2 = "/home/shiva/Downloads/resumes/Azhar khan.pdf"

path3 = "/home/shiva/Downloads/resumes/Abhishek Gunda.pdf"

 

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

path15 = "/home/shiva/Downloads/resumes/MukarramSultan_Resume1-1.pdf"
 
path16  = "/home/shiva/Downloads/resumes/Nangi Ramesh.pdf"

path17 = "/home/shiva/Downloads/resumes/Venkata Reddy Yeruva.pdf"

if __name__== '__main__':  
   pipeline_start(path16)
   