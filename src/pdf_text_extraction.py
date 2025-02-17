import pdfplumber
import pymupdf
import fitz
import io  





#Extracts all the text from a given PDF file using pdfplumber.
def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pf:
        extracted_text =" "
        for page in pf.pages:
            extracted_text+=page.extract_text()
    
    return extracted_text        
            

  
     
#Extracts all the text from a given PDF file using pymupdf.
def extract_text(path):
    
    extracted_text =""
    extract_text_list = []
    
 
    if isinstance(path, str):  
        doc = fitz.open(path)
    else:
        file_stream = io.BytesIO(path.read())  
        doc = fitz.open(stream=file_stream, filetype="pdf")
    
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



path1="/home/shiva/Downloads/resumes/Nangi Ramesh.pdf"
path8 = "/home/shiva/Downloads/resumes/Swpana Kumari Sahu.pdf"
path5 = "/home/shiva/Downloads/resumes/Ketan Gwari.pdf"

# extract_text(path5)

def extract_text_for_cer(path):
    
    if isinstance(path, str)==False:
        path.seek(0)

    extracted_text = ""
    extract_text_list = []
    
    if isinstance(path, str):  
        doc = fitz.open(path)
    else:
        file_stream = io.BytesIO(path.read())  
        doc = fitz.open(stream=file_stream, filetype="pdf")
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]  
        
        for block in blocks:
            if block['type'] == 0: 
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span['text']
                        if text == " ":
                            continue
                        if 'bold' in span['font'].lower():
                            is_bold = True
                        else:
                            is_bold = False

                        if is_bold:
                            k=1
                        else:
                            k=0

                        extract_text_list.append((text, k))
                        extracted_text += text + "\n"
    
    return extracted_text, extract_text_list


