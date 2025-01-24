import re
import nltk
from nltk import pos_tag,ne_chunk
from nltk.tokenize import WhitespaceTokenizer
import spacy
from transformers import pipeline    



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
        if i>10:
            break
        elif token.pos_ in ['PROPN']:
            txt=txt+" "+token.text
            i+=1
    print(txt)
    
    doc1=nlp(txt)
    i=1
    txt1=""      
    for ent in doc.ents:
        if (i>10):
            break
        if ent.label_ not in ['PERSON']:
            txt1=txt1+" "+ent.text
            i=i+1
    print(txt1)
    
    
    txt = (txt.lower()).split()
    txt1 = (txt1.lower()).split()
    
    print(txt)
    print(txt1)
                    
    for word1 in txt1:
        txt = [word for word in txt if word != word1]
        
    str=""
    for word in txt:
        str=str+" "+word
        
           
            
            
    return str
    
    
def name_extract(text):    
    
    txt = name_tagging(text)    
    
    model =pipeline("text2text-generation",model="google/flan-t5-large")
    
    instruction="Extract the only name of the person from the resume:"
    
    input_text=f"{instruction}\n{txt}"

    response=model(input_text,max_length=50,do_sample=False)
    
    print(response)
    
    
    #the bachelors or masters
def education_extract(text):    
    
    # txt = name_tagging(text)    
    
    model =pipeline("text2text-generation",model="google/flan-t5-large")
    
    instruction="extract the bachelors or masters education details of the person"
    
    input_text=f"{instruction}\n{text}"

    response=model(input_text,max_length=50,do_sample=False)
    
    print(response)    



    
    


def experience_extract(lines):
    pattern = r"\d{1,2}\+?\s?years"
    for line in lines:
        if 'experience' in line.lower():
            exp = re.findall(pattern,line)
            if len(exp)>0:
                return exp
    
            
            
       