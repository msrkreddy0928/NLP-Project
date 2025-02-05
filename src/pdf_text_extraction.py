import pdfplumber
import pymupdf
import fitz
import io  
import pymupdf4llm
from llama_index.embeddings import HuggingFaceEmbedding


embed_model = HuggingFaceEmbedding(model_name="HuggingFaceH4/zephyr-7b-alpha")


# pipe = pipeline("text-generation", model=)
# pipe("pipe",messages)



# path3 = "/home/shiva/Downloads/resumes/Abhishek Gunda.pdf"

# path3 = "/home/shiva/Downloads/resumes/Azhar khan.pdf"

# md_text = pymupdf4llm.to_markdown(path3)

# # print(md_text)

# llama_reader = pymupdf4llm.LlamaMarkdownReader()
# llama_docs = llama_reader.load_data(path3)

# print(llama_docs)



def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pf:
        extracted_text =" "
        for page in pf.pages:
            extracted_text+=page.extract_text()
    
    return extracted_text        
            
            
# path4 = "/home/shiva/Downloads/resumes/Dhananjay Kumar Yadav.pdf" 
# #path9 = "/home/shiva/Downloads/resumes/Kashetti_Venu.pdf"


# path10 = "/home/shiva/Downloads/resumes/Dublin-Resume-Template-Modern.pdf"    

     

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



# extract_text(path3)




