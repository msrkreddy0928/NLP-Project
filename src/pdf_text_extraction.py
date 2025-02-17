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

# doc = pymupdf.open(path5)
# header = "Header"  # text in header
# footer = "Page %i of %i"  # text in footer
# for page in doc:
#     page.insert_text((50, 50), header)  # insert header
#     page.insert_text(  # insert footer 50 points above page bottom
#         (50, page.rect.height - 50),
#         footer % (page.number + 1, doc.page_count),
#     )
#     print(page.get_textbox(rect=True))


import fitz

doc = fitz.open(path8)
page = doc[0] 
if page.annots():
    annotations = list(page.annots())
    print(annotations)
    first_annot = page.first_annot
    rect = first_annot.rect 
    text = page.get_textbox(rect) 


print(page.get_textbox(rect))

