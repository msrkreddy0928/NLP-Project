import pdf_text_extraction
from pdf_text_extraction import extract_text_from_pdf
from preprocessing import text_to_words,split_lines
from feature_extraction import phone_num_extrcat,name_extract,experience_extract,education_extract


def pipeline(path):
   
   text = extract_text_from_pdf(path)

   words = text_to_words(text)
   
   lines = split_lines(text)
   
   phone_num =  phone_num_extrcat(text)      
  
   exp=experience_extract(lines)
   
   name = name_extract(text)
   
   index=0
   for line in lines:
      if 'education' in line.lower():
         index = lines.index(line)
         break
         
   education = education_extract(lines[index:index+20])
   
   print(name)
   print(phone_num)
   print(exp)
   print(education)
   
   if exp ==None:
      exp = "Experience not found"
   
   return name,phone_num,exp,education
   
   


path0 = "/home/shiva/Downloads/resumes/Untitled design.pdf"

path1 = "/home/shiva/Downloads/resumes/London-Resume-Template-Professional.pdf" 

path2 = "/home/shiva/Downloads/resumes/Abhishek Gunda.pdf"

path3 = "/home/shiva/Downloads/resumes/Azhar khan.pdf" 

path4 = "/home/shiva/Downloads/resumes/Dhananjay Kumar Yadav.pdf" 

path5 = "/home/shiva/Downloads/resumes/Ketan Gwari.pdf"

path6 = "/home/shiva/Downloads/resumes/Nanneboina Ramana.pdf"

path7 = "/home/shiva/Downloads/resumes/Shaik Luqman.pdf"

path8 = "/home/shiva/Downloads/resumes/Swpana Kumari Sahu.pdf"   

if __name__== '__main__':
   pipeline(path2)