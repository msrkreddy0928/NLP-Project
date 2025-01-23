import re
import nltk
from nltk import word_tokenize,pos_tag,ne_chunk
from nltk.tokenize import WhitespaceTokenizer
import spacy

nltk.download('punkt')          
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab') 
nltk.download('words')


def phone_num_extrcat(words):
    
    for word in words:
        match=re.match("^\d.*",word)
        if (match and len(word)>=10):
            return word
        
        
def name_extract(lines):
    if ',' in  lines[0]:
        index=lines[0].index(',')
        return lines[0][:index]
    else:
        return lines[0]        