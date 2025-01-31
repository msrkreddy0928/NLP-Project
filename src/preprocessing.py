from nltk import word_tokenize,pos_tag,ne_chunk
import spacy
import re

def text_to_words(text):
    words=word_tokenize(text)
    
    return words

def words_tagging(words):
    tagged_words = pos_tag(words)
    return tagged_words
    


def split_lines(text):
    lines = text.splitlines()
    return lines


def line_remover(text_list):

    for i,line in enumerate(text_list):
        text_list[i] = re.sub("\n",',',line)
        
    text_list = [line for line in text_list if line != ' ,']    

    return text_list          
             
    