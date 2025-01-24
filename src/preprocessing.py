from nltk import word_tokenize,pos_tag,ne_chunk
import spacy

def text_to_words(text):
    words=word_tokenize(text)
    
    return words

def words_tagging(words):
    tagged_words = pos_tag(words)
    return tagged_words
    


def split_lines(text):
    lines = text.splitlines()
    return lines

