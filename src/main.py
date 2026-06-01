from ingestion.pdf_loader import BasePDFLoader
from core.config import SOURCE_DOCUMENTS

loader=BasePDFLoader()
text=loader.load(str(SOURCE_DOCUMENTS/"test.pdf"))
print(text[:1000])
print()
print(len(text))