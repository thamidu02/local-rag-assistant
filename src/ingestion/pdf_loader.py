from pypdf import PdfReader
from ingestion.base_loader import BasedocumentLoader

class BasePDFLoader(BasedocumentLoader):
    
    def load(self,file_path:str)->str:
        reader=PdfReader(file_path)
        text=""
        
        for page in reader.pages:
            page_text=page.extract_text()
            
            if page_text:
                text+=page_text+ "\n"
                
        return text
    
    
class ArxivPDFLoader(BasedocumentLoader):
    pass