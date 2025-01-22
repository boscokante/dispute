import pdfplumber
from typing import List, Optional
import re

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from each page of a text-based PDF and return a single string."""
    text_content = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_content.append(page_text)
    return "\n".join(text_content)

def extract_report_date(pdf_text: str) -> Optional[str]:
    """
    Extract report date from Equifax report text, typically found at bottom of pages
    """
    # Look for date patterns like "Report Date: MM/DD/YYYY" or similar
    date_patterns = [
        r"Report Date:\s*(\d{1,2}/\d{1,2}/\d{4})",
        r"Report Date:\s*(\d{1,2}-\d{1,2}-\d{4})",
        r"Date:\s*(\d{1,2}/\d{1,2}/\d{4})"
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, pdf_text)
        if match:
            return match.group(1)
    
    return None