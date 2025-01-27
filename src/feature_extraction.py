import re
import nltk
from nltk import pos_tag,ne_chunk
from nltk.tokenize import WhitespaceTokenizer
import spacy
from transformers import pipeline    
from datetime import date


nltk.download('punkt')          
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab') 
nltk.download('words')

nlp = spacy.load("en_core_web_sm")


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
    # txt1 = (txt1.lower()).split()
    # print(txt)
    # print(txt1)
  
                    
    for word1 in txt:
        if '@' in word1:
            txt.remove(word1)
            
        
    # str=""
    # for word in txt:
    #     str=str+" "+word
        
    # print(str)       
    return txt
    
    
def name_extract(text):    
    
    txt = name_tagging(text)    
    
    model =pipeline("text2text-generation",model="google/flan-t5-large")
    
    instruction="Extract only full name of the person from the resume:"
    
    input_text=f"{instruction}\n{txt}"

    response=model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']
    
    return response
    

def pass_out_year_extract(lines):
    
    lines = education_text(lines)
    pattern = r"\d{2,4}"  
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
 
    
    
      
def education_text(lines):
     
    index=0
    for line in lines:
      if ('Education' in line) or ('EDUCATION' in line):
         index = lines.index(line)
         break
     
    return lines[index:index+20]     
        
        
    
    
def education_extract(lines):
    
    text =education_text(lines)

    model =pipeline("text2text-generation",model="google/flan-t5-large")
    
    instruction="extract the Education or EDUCATION details of the person from the resume"
    
    input_text=f"{instruction}\n{text}"

    response=model(input_text,max_length=50,do_sample=False)
    
    response = response[0]['generated_text']

    return response    
  

def degree_extraction(text):
    
    degree_set = ['Masters',"Master","Bachelor","Bachelors","BA","ARTS","MTech","BTech","Associate","BE" ]
    degree_set_1 =['ma','ba','mt','bt','be','ar','m','b','p','g']
    txt= text.split()
    degree=""
    
    for i, word in enumerate(txt):
        txt[i] = re.sub(r'[^a-zA-Z0-9,]', '', word)
        if txt[i]=='':
            txt.remove(txt[i])
        
    
    for word in txt:
        
        print((word[:2]).lower())
        if (word[:2]).lower() in degree_set_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           :
            k=0
            for d_word in txt[txt.index(word):]:
                degree=degree+" "+d_word
                if d_word[-1] ==',':
                    k=k+1
                print(k)    
                if k==2:
                    break
               
            if k==2:
                break
            
              
                  
            
    print(degree)
    
    return degree       
            

       
  
  




def experience_extract(lines):
    
    pattern = r"\d{1,2}\+?\s?years"
    for line in lines:
        if 'experience' in line.lower():
            exp = re.findall(pattern,line)
            if len(exp)>0:
                return exp[0]
            
    
            
            
       