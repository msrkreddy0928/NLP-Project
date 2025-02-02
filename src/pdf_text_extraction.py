import pdfplumber
import pymupdf
import fitz  

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pf:
        extracted_text =" "
        for page in pf.pages:
            extracted_text+=page.extract_text()
    
    return extracted_text        
            
            
# path4 = "/home/shiva/Downloads/resumes/Dhananjay Kumar Yadav.pdf" 
# #path9 = "/home/shiva/Downloads/resumes/Kashetti_Venu.pdf"
# path3 = "/home/shiva/Downloads/resumes/Azhar khan.pdf"

# path10 = "/home/shiva/Downloads/resumes/Dublin-Resume-Template-Modern.pdf"         

def extract_text(path):
    
    extracted_text =""
    extract_text_list = []
    
    doc = fitz.open(path)
    
    for page_num in range(len(doc)):
        
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")      
        # get_text("blocks")
        for block in blocks:
            x0, y0, x1, y1, text,k,l= block
            # print(f"Text: {text}, Position: {x0}, {y0}, {x1}, {y1}",{k},{l})
            if text == "":
                continue
            extract_text_list.append(text)
            extracted_text += text + "\n"
           

    return extracted_text,extract_text_list


# def extract_text(path):
#     extracted_text = ""
#     doc = fitz.open(path)

#     for page_num in range(len(doc)):
#         page = doc.load_page(page_num)
#         text = page.get_text("text")
#         # print(text)
        
#         # Extract all text at once

#         extracted_text += text

#     return extracted_text







# print(extract_text)
# path6 = "/home/shiva/Downloads/resumes/Nanneboina Ramana.pdf"
path6 = "\\Users\\Shiva Reddy\\Downloads\\resumes\\Nanneboina Ramana.pdf"
# extract_text(path6)

# extract_text =""
# doc = fitz.open(path3)

# for page_num in range(len(doc)):

#     page = doc.load_page(page_num)
    
#     text_dict = page.get_text("dict")
    
#     for block in text_dict["blocks"]:
#         if block["type"] == 0: 
#             # print("Block bbox:", block["bbox"]) 
#             for line in block["lines"]:
#                 for span in line["spans"]:
#                     print("Text:", span["text"])  
                    
                     
                     
                    
#                     print("Position (bbox):", span["bbox"])  
