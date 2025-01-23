import pdfplumber

def extract_text_from_pdf(path):
    with pdfplumber.open(path) as pf:
        extracted_text =" "
        for page in pf.pages:
            extracted_text+=page.extract_text()
    
    return extracted_text        
            