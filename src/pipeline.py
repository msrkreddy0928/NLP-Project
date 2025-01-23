from pdf_text_extraction import extract_text_from_pdf
from preprocessing import text_to_words,split_lines
from feature_extraction import phone_num_extrcat,name_extract

def pipeline(path):
   text = extract_text_from_pdf(path)
   words = text_to_words(text)
   lines = split_lines(text)
   phone_num =  phone_num_extrcat(words)
   name = name_extract(lines)
   
   print(phone_num)
   print(name)
   
   







path = "/home/shiva/Downloads/Untitled design.pdf"

path1 = "/home/shiva/Downloads/London-Resume-Template-Professional.pdf"   
   
   
if __name__ =="__main__":
    pipeline(path)   