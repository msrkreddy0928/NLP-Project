import re
import spacy
from transformers import pipeline    
from datetime import date

nlp = spacy.load("en_core_web_sm")


ext_degree =""



def phone_num_extrcat(text):
    pattern = r"\(?\+?\(?\d{1,3}\)?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}"
    numbers = re.findall(pattern, text)
    if len(numbers)<1:
        return "valid number not found"
    k=0
    for num in numbers:
        if(len(num)>=10):
            k+=1
            return num
    if k==0:
        return "valid number not found"
  
    
    
def name_tagging(text):
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
    
    
def name_extract(text,model):    
    
    txt = name_tagging(text)    
    
    instruction="Extract the only full name of the person from the resume:"
    
    input_text=f"{instruction}\n{txt}"

    response=model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']
    
    return response
    

def pass_out_year_extract(lines):
    
    # print(lines)
    lines = education_text(lines)
    pattern = r"\d{2,4}"  
    for line in lines:
        year = re.findall(pattern,line)
        print(year)
        if len(year)>0:
            break
     
    # match = re.findall(pattern,lines)
    
    # print(match) 
    # year =0
        
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
 
    
    
      
def education_text(lines):
     
    index=0
    for line in lines:
      if ('Education' in line) or ('EDUCATION' in line):
         index = lines.index(line)
         break
    return lines[index:index+20]     
        
        
    
def education_extract(lines,model):
    
    text =education_text(lines)
    
    instruction ="extract the Education or EDUCATION details of the person from the resume"
    
    input_text=f"{instruction}\n{text}"

    response=model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']
    
    print("edication extract",response)
    

    return response    
  

def degree_extraction(text):

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
     
     
    print("dict1",dict1) 
             
    # global ext_degree
    
    # ext_degree= dict1["pg"]
    
    return dict1
 
         

def extract_degree2(lines,model):
    
    lines = education_text(lines)
         
    text = lines     
    instruction= "Extract all the educational degrees mentioned in the education section from the provided text. Provide the degrees exactly as they appear."
    # instruction = "extract the all educational degrees as it is from the education section "
    
    input_text = f"{instruction}\n{text[:15]}"

    response = model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']     
    
    print(response)
       
    
    return response








       
def college_extraction(lines,model,degree1,degree2):
    
      lines =education_text(lines)     
      college_list = ["college","university","technology","institute","school"]
      
      text=""
      
  
      
      
      instruction="extract the latest or first occurance of college or university names  in Education or EDUCATION section of the person from the resume"
    
      input_text=f"{instruction}\n{lines[:20]}"

      response=model(input_text,max_length=50,do_sample=False)
    
      response = response[0]['generated_text']
      
      print("COLLEGE",response)
      
      degree=None
      
      if degree1 is None or degree2 is None:
          degree = degree_extraction(response)
             
      
      txt =(response.lower()).split()
 
      if "college"  not in txt:
          for word in txt:
              if word in ["jntu"]:
                  return word,degree
          
    
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
      
      
      print(college2)       
              
            

      
      return college1,college2,degree
    



def experience_extract(lines):
    
    pattern = r"\d{1,2}\+?\s?years"
    for line in lines:
        if 'experience' in line.lower():
            exp = re.findall(pattern,line)
            if len(exp)>0:
                return exp[0]
            
            

    
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
    
    # print(start_index)
    break_list =[r"EXPERIENCE\s*:?",r"Experience\s*:?",r"HISTORY\s*:?",r"History\s*:?",r"Skills\s*:?",r"SKILLS\s*:?",r"Education\s*:?",r"EDUCATION\s*?"]

        
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
        
 
    str = ""
    for word in summary:
        str=str+" "+word
        
    
    
    return str            
    
               
        
        
   
            
   