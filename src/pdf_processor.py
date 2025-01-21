import pdfplumber
from typing import List

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from each page of a text-based PDF and return a single string."""
    text_content = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_content.append(page_text)
    return "\n".join(text_content)