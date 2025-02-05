import re
import spacy
from transformers import pipeline    
from datetime import date
import os 
import sys
sys.path.append("/home/shiva/Desktop/ML/Files/NLP")
from skills import skills_1
import json   


ext_degree =""
nlp = spacy.load("en_core_web_sm")


def extract_phone_num(text):
    pattern = r"\(?\+?\(?\d{1,3}\)?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}"
    numbers = re.findall(pattern, text)
    if len(numbers)<1:
        return "valid number not found"
    k=0
    for num in numbers:
        if(len(num)>=10):
            k+=1
            return num[len(num)-10:],num[:len(num)-10]
    if k==0:
        return "valid number not found"
  
    
    
def name_tagging(text):
    
    words_to_search = [r"profile\s*:?",r"objective\s*:?",r"summary\s*:?",r"about\s*"]
    
    
    # for word in words_to_search:
    #     match = re.findall(word,text)
    #     if match:
    #         index = text.find(match[0])
    #         text=text[:index]
    #         break
     
    
    doc = nlp(text)
    txt="" 
    i=1  
    for token in doc:
        if i>6:
            break
        elif token.pos_ in ['PROPN']:
            txt=txt+" "+token.text
            i+=1
    
    i=1
    txt1=""      
    for ent in doc.ents:
        if (i>10):
            break
        if ent.label_ not in ['PERSON']:
            # print(ent.text,ent.label_)
            txt1=txt1+" "+ent.text
            i=i+1
            
    
    txt = txt.split()
  
                    
    for word1 in txt:
        if '@' in word1:
            txt.remove(word1)
            
        
    str=""
    for word in txt:
        str=str+" "+word
         
    return str
    
    
def extract_name(text,model):    
    
    txt = name_tagging(text)   
    
    instruction="Extract the only full name of the person from the resume:"
    
    input_text=f"{instruction}\n{txt}"

    response=model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']

    return response
    

def pass_out_year_extract(lines):
    

    lines = extract_education_text(lines)
    pattern = r"-?\d{2,4}-?"  
    for line in lines:
        year = re.findall(pattern,line)
        if len(year)>0:
            break
     
    year = str(year[-1])    
    current_date = date.today()
    current_year = current_date.year
    current_year = int(str(current_year)[2:])
    
    if len(year)==2:
         if int(year)>current_year:
             year = "19"+year
         else:
             year= "20"+year  
             
        
    return year
 
    
    
      
def extract_education_text(lines):
    index=0
    for line in lines:
        # print("line ",line)
        if ('Education' in line) or ('EDUCATION' in line) or ('QUALIFICATION' in line):
         index = lines.index(line)
         break
     
     
    return lines[index:index+20]     
        
        
    
def extract_education(lines,model):
    
    # text =education_text(lines)
    
    #"extract the Education or EDUCATION details of the person from the resume"
    
    instruction ="extract the Education or EDUCATION details of the person from the resume"
    
    input_text=f"{instruction}\n{lines}"

    response=model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']
    
    print("education extract",response)

    return response 


def extract_education_1(lines,model):
    
    # lines = education_text(lines)
         
    text = lines     
    instruction = "Extract all the educational degrees mentioned in the education section from the provided text. Provide the degrees exactly as they appear."
    # instruction= "Extract all the  educational degrees with colleges years and percenatges under education section as it is from the resume "
    # instruction = "extract degree,college name,pass out year,percentage or cgpa in the form of dictionary (college,name,pass out year,cgpa)as key values  from education section"
    
    input_text = f"{instruction}\n{text}"

    response = model(input_text,max_length=100,do_sample=False)

    print("educationresponse",response)
    
    response = response[0]['generated_text']     
    
   
       
    
    return response
   
  

def extract_degree(text):

    degree_set_pg =("m.","m.tech","mtech","master","masters","post","m.a")
    degree_set_grad = ("bachelor","bachelors","arts","b.tech","btech","ba","be","b.","b.e","b.a")
    
    txt= text.split()
    degree=""
    dict1={"pg":None,"grad":None}
    
    for i, word in enumerate(txt):
        txt[i] = re.sub('[^A-Za-z0-9,.]', '', word)
        if txt[i]=='':
            txt.remove(txt[i])
        
    degree=""
    for word in txt:
        if (word.lower()).startswith (degree_set_pg):
            degree=word
            if word.lower() in ["m.","post"]:
                degree=degree+" "+txt[txt.index(word)+1]
         
            
            
        if len(degree)>0:
                dict1["pg"]=degree
                break
    #     # return degree
    
    degree=""
    for word in txt:
        if (word.lower()).startswith (degree_set_grad):
            degree=word
            if word.lower() in ["b.","under"]:
                 degree=degree+" "+txt[txt.index(word)+1]
              
           
        if len(degree)>0:
            dict1["grad"]=degree
            break
     
     
  
             
    # global ext_degree
    
    # ext_degree= dict1["pg"]
    
    return dict1
 


def extract_degree_1(text):
    
    degree_set_pg =("m.","m.tech","mtech","master","masters","post","m.a")
    degree_set_grad = ("bachelor","bachelors","arts","associate","b.tech","btech","ba","be","b.","b.e","b.a")
    
    txt= text.split(",")
    
    print("txt",txt)
    degree=""
    dict1={"pg":None,"grad":None}
    
    for i, word in enumerate(txt):
        txt[i] = re.sub('[^A-Za-z0-9,." "]', '', word)
        if txt[i]=='':
            txt.remove(txt[i])
        
    degree=""
    for word in txt:
            for deg in degree_set_pg:
                word = word.lstrip()
                if word.lower().startswith(deg):
                    degree=word
                    break
            
         
            if len(degree)>0:
                dict1["pg"]=degree
                break

    
    degree=""
    for word in txt:
        word = word.lstrip()
        if (word.lower()).startswith (degree_set_grad):
            degree=word
           
        if len(degree)>0:
            dict1["grad"]=degree
            break
        

    
    return dict1    
        
     




def  extract_passout(lines,degree1,degree2):
    
    index=-1
    
    if degree1 is not None:
        index = lines.find(degree1)
        if index>-1:
            lines1=lines[index:]
            lines1=lines1.split()
            txt=""
            for i,line in enumerate(lines1[1:]):
                txt=txt+" "+line
                if i==4:
                    break
                
            pattern = r"\d{4}"      
    
            match = re.findall(pattern,txt)
    
            print("match1",match)
    
    if degree2 is not None:
         index = lines.find(degree2)
         if index>-1:
            lines2=lines[index:]
            lines2=lines2.split()
            txt=""
            for i,line in enumerate(lines2[1:]):
                txt=txt+" "+line
                if i==4:
                    break
                
            pattern = r"\d{4}"      
    
            match = re.findall(pattern,txt)
    
            print("match2",match)
             
    
    
    return

    

def extract_passout_1(text,degree1,degree2):
    
    pattern = r"-?\d{4}-?" 
    
    pass_out_year_1=None
    pass_out_year_2=None
    text_college_1=None
    text_college_2=None
     
    ind = text.lower().find('experience')
    if ind>-1:
        text=text[:ind]

    if degree1 is not None:
        
        degree1_1 = degree1.split()
        degree1_1=degree1_1[0]
        index = text.find(degree1_1)
        if degree2 is not None:
            degree2_2 = degree2.split()
            degree2_2 = degree2_2[0]
            index_1 = text.find(degree2_2)
            if index>index_1:
                text_college_1=text[index+len(degree1):]
                text_college_2=text[index_1+len(degree2):index]
            else:
                text_college_1=text[index+len(degree1):index_1]
                text_college_2=text[index_1+len(degree2):]    
        else:
            text_college_1 = text[index+len(degree1):]    
    
    elif degree2 is not None:
        
        degree2_2 = degree2.split()
        degree2_2 = degree2[0]
        index_1 = text.find(degree2_2)
        text_college_2=text[index_1+len(degree2):]
    
    college_list = ["college","university","technology","institute","school"]

    if text_college_1 is not None:
        pass_out_year_1 = re.findall(pattern,text_college_1)
        if len(pass_out_year_1)>=2:
            index1 = text_college_1.find(pass_out_year_1[0])
            index2 = text_college_1.find(pass_out_year_1[1])
            if index2-index1<=30:
                pass_out_year_1=pass_out_year_1[1]
            else:
                pass_out_year_1=pass_out_year_1[0]    
           
        elif len(pass_out_year_1)==1:
            pass_out_year_1=pass_out_year_1[0]
        else:
            pass_out_year_1=None    
    
    
    
    if text_college_2 is not None:
        pass_out_year_2 = re.findall(pattern,text_college_2)
        if len(pass_out_year_2)>=2:
            index1 = text_college_2.find(pass_out_year_2[0])
            index2 = text_college_2.find(pass_out_year_2[1])
            if index2-index1<=30:
                pass_out_year_2=pass_out_year_2[1]
            else:
                pass_out_year_2=pass_out_year_2[0]    
           
        elif len(pass_out_year_2)==1:
            pass_out_year_2=pass_out_year_2[0]
        else:
            pass_out_year_2=None    
        
 
  

    

    return pass_out_year_1,pass_out_year_2



def extract_college_1(lines,model,degree1,degree2):
    
    college_list = ["college","university","technology","institute","school"]
      
    instruction="extract the latest or first occurance of college or university names  in Education or EDUCATION section of the person from the resume"
    
    input_text=f"{instruction}\n{lines}"

    response=model(input_text,max_length=80,do_sample=False)
    
    response = response[0]['generated_text']
    
    print("college",response)
    
    response_list = response.split()
    
    
    college1 = None
    college2 = None
    

    if degree1 is not None:
        degree = degree1.split()
        if response_list[0][-3:]==degree[0][-3:]:
            index = response.find(",")
            college1 = response[index+1:]
            response2=response[index+1:]
        else:
            college1=response
            response2=response
        k=0   
        for word in college_list:
            index = (college1.lower()).find(word)
            if index>-1:
                college1=college1[:index+len(word)]
                k+=1    
                break
        if k==0:
            index = college1.index(",")
            if index>-1:
                college1=college1[:index]
            else:
                college1 = college1
                
        if degree2 is not None:
            response2 = response2.replace(college1,'')
            college2 = response2
            print("rep",response2)
                  
        
    elif degree2 is not None:
         degree = degree2.split()
         if response_list[0][-3:]==degree[0][-3:]:
            index = response.find(",")
            college2 = response[index+1:]
         else:
             college2=response
         k=0    
         for word in college_list:
            index = (college2.lower()).find(word)
            if index>-1:
                college2=college2[:index+len(word)]
                k+=1    
                break    
         if k==0:
             index = college2.find(",")
             if index>-1:
                 college2=college2[:index]
             else:
                 college2 = college2
            

   
    
    return college1,college2
       
        
           

    


def extract_college(lines,model,degree1,degree2):
    
      lines = extract_education_text(lines)
      college_list = ["college","university","technology","institute","school"]
      
      instruction="extract the latest or first occurance of college or university names  in Education or EDUCATION section of the person from the resume"
    
      input_text=f"{instruction}\n{lines}"

      response=model(input_text,max_length=80,do_sample=False)
    
      response = response[0]['generated_text']
      
      print("COLLEGE",response)
      
      degree=None
      
      if degree1 is None or degree2 is None:
          degree = extract_degree(response)
             
      
      txt =(response.lower()).split()
          
    
      index = response.find(",")
      
   
      college1 = response
      if index>-1:
          college1 = response[:index]
          
      
      college2 = response[index+1:]
      print("college2",college2)    
      
    
      college_list = ["college","university","technology","institute","school"]
      
      for word in college_list:
          index = (college1.lower()).find(word)
          if index>-1:
              college1 = college1[:index+len(word)]
              break
          
      for word in college_list:
          index = (college2.lower()).find(word)
          if index>-1:
              index_1 = college2[:index+len(word)].find(',')
              college2 = college2[index_1+1:index+len(word)]
              break 
         

      
      return college1,college2,degree
    



def extrcat_experience(lines):
    
    pattern = r"\d{1,2}\+?\s?years"
    for line in lines:
        if 'experience' in line.lower():
            exp = re.findall(pattern,line)
            if len(exp)>0:
                return exp[0]
            
 
 
 
 
def extract_experience_1(text):
    pattern = r"\d{1,2}\+?\s?years"
    
    exp = re.findall(pattern,text)
    
    
    if len(exp)>0:
        return exp[0]
    
    else:
        return None            



def extract_percentage(text):
    
    #  print("text",text)
     pattern = r"^\s*([+-]?\d+(\.\d+)?%)\s*$"

    
     percent = re.findall(pattern,text)
     
     print("percent",percent)
    




def extract_summary_1(text):
    
    start_index=-1
    lines = text.splitlines()

    
    summary =""
     
    words_to_search = [r"profile\s*:?",r"objective\s*:?",r"summary\s*:?",r"about\s*"]
    
    for i,line in enumerate(lines):
        for word in words_to_search:
            match = re.findall(word,line.lower())
            if len(match)>0:
                start_index=i
                break
        if start_index>-1:
            break
        
    break_list = [r"\bEXPERIENCE\b\s*:?", r"\bExperience\b\s*:?", r"\bHISTORY\b\s*:?",  r"\bHistory\b\s*:?", r"\bSkills\b\s*:?", r"\bSKILLS\b\s*:?",  r"\bEducation\b\s*:?", r"\bEDUCATION\b\s*?"]

        
    if start_index>-1:
        k=0
        for line in lines[start_index:]:
            for word in break_list:
                match= re.findall(word,line)
                if len(match)>0:
                    k+=1
                    break    
            if k>0:
                break
            else:
                summary = summary+" "+line
                
                
    summary = summary.lstrip()
    
    summary1 = summary.split()
    
    words_to_search = ["profile","profile:","professional","objective","objective:","career","career:","summary","summary:","about" "me","me:"]                   
    
    
    for wd in summary1[:4]:
        for word in words_to_search:
            if wd.lower() == word:
                summary1.remove(wd)
                break 
    
    
    summary = ' '.join(summary1)    
        
    
    print(summary)

    return summary   
    



def extract_summary(lines,name,phoneNo):
    
    start_index=-1
    summary =""
    
    lines = lines[:30]
    
    words_to_search = [r"profile\s*:?",r"objective\s*:?",r"summary\s*:?",r"about\s*"]
    
    
    for i,line in enumerate(lines):
        for word in words_to_search:
            match = re.findall(word,line.lower())
            if len(match)>0:
                start_index=i
                break
        if start_index>-1:
            break
    

    break_list = [r"\bEXPERIENCE\b\s*:?", r"\bExperience\b\s*:?", r"\bHISTORY\b\s*:?",  r"\bHistory\b\s*:?", r"\bSkills\b\s*:?", r"\bSKILLS\b\s*:?",  r"\bEducation\b\s*:?", r"\bEDUCATION\b\s*?"]

        
    if start_index>-1:
        k=0
        for line in lines[start_index:start_index+20]:
            for word in break_list:
                match= re.findall(word,line)
                if len(match)>0:
                    k+=1
                    break    
            if k>0:
                break
            else:
                summary = summary+" "+line        

    
    if len(summary)>1:
        summary = summary.split()
        list1 = [phoneNo]
        list1=list1+name.split()
        for word in list1:
            for txt in summary:
                if word in txt or "@" in txt:
                    summary.remove(txt)
                    
        summary = summary[1:]
        
        if summary[-1][-1]!=".":
            summary.remove(summary[-1])
        
 
  
   
    words_to_search = ["profile","profile:","professional","objective","objective:","career","career:","summary","summary:","about" "me","me:"]         
      
    for wd in summary[:4]:
        for word in words_to_search:
            if wd.lower() == word:
                summary.remove(wd)
                break 
    
    
    summary = ' '.join(summary)    
        
    
    return summary         
    
               
        
        
def extract_certifications(lines):
    
    certification_text = None
    
    for line in lines:
        if "certification" in line.lower() or "courses" in line.lower():
            index = lines.index(line)
            certification_text = lines[index:]
            break
        
    print("cer",certification_text[1:3])    
            


def extract_email(text):
    
    email = None
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.?[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    else:
        doc = nlp(text)
        for token in doc:
            if token.like_email:
                email = token.text
                break
    email = email or "Email not found"
    
    return email
    
    

   
            
KNOWN_TITLES_FILE = "known_job_titles.json"
 
# Load known job titles
if os.path.exists(KNOWN_TITLES_FILE):
    try:
        with open(KNOWN_TITLES_FILE, "r") as file:
            known_job_titles= set(json.load(file))  # Load as a set for quick lookup
    except (json.JSONDecodeError, ValueError):
        print(f"Warning: {KNOWN_TITLES_FILE} contains invalid JSON. Initializing an empty set.")
        known_job_titles= set()
else:
    known_job_titles= {"Software Engineer", "Software Developer", "AI Developer", "Data Scientist", "Project Manager", "Web Developer", "Business Analyst"}
 
 
 
  
 
# Extract job title from known titles
def extract_title(text,model):
    
    for title in known_job_titles:
        if title.lower() in text.lower():
            return title
        
    
    job_title_prompt = f"Extract the job title from the following resume text. Return only the job title.\n{text}"
    response = model(job_title_prompt, max_length=100, num_return_sequences=True)
    response = response[0]['generated_text']
    
    return response
 


# Add a new job title to the known job titles
def add_title(job_title):
    if job_title not in known_job_titles:
        known_job_titles.add(job_title)
        save_known_job_titles(known_job_titles)   
                              
 
def save_known_job_titles(known_job_titles, KNOWN_TITLES_FILE="known_job_titles.json"):
    """Save the updated set of job titles to the JSON file."""
    with open(KNOWN_TITLES_FILE, "w") as file:
        json.dump(list(known_job_titles), file)
        
        
def extract_organization(text):
 
    keywords=['Work History','Employment','Professional Background','Work Experience','Professional Experience','Employment History',
          'EXPERIENCE','WORK HISTORY','EMPLOYMENT','PROFESSIONAL BACKGROUND','WORK EXPERIENCE','PROFESSIONAL EXPERIENCE','EMPLOYMENT HISTORY','Experience']    
    for keyword in keywords:
        if keyword in text:
            start = text.find(keyword)
            return text[start:start + 700]
        return text
            

def extract_latest_organization(text,model):
    
    text = extract_organization(text)

    
    organization_prompt = f"From the following resume text, extract the name of the most recent organization the candidate has worked for. Focus only on work history and return the organization name \n{text}"
    response = model(organization_prompt, max_length=100, num_return_sequences=True)
    response = response[0]['generated_text']
    
    return response

 



def extract_skills(text):
    extracted_skills = {category: set() for category in skills_1}
 
    for category, skill_list in skills_1.items():
        for skill in skill_list:
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, text.lower()):
                extracted_skills[category].add(skill)
 
    return {category: ",".join(skill_set) if skill_set else "None" for category, skill_set in extracted_skills.items()}


# from skillID import skills_dict
# import re
# def extract_skills(text):
#     skills_found=[]
#     for category,skills in skills_dict.items():
#         for skill,skill_id in skills.items():
#             if re.search(r"\b"+re.escape(skill)+r"\b",text,re.IGNORECASE):
#                 skills_found.append({
#                 'skillCategory':category,
#                 'skillCategoryID':skill_id
#             })
#     return skills_found                              