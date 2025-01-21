from pdf_processor import extract_text_from_pdf
from gpt_analyzer import step_a_identify_detailed_errors, step_b_format_final
import os

def analyze_credit_report(pdf_path: str) -> str:
    """
    Analyze a credit report PDF and generate a dispute letter.
    """
    # Expand user path and clean it
    pdf_path = os.path.expanduser(pdf_path.strip('" '))
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # Step A: Identify detailed errors
    detailed_errors = step_a_identify_detailed_errors(pdf_text)
    
    # Step B: Format final dispute letter
    final_letter = step_b_format_final(detailed_errors)
    
    return final_letter

if __name__ == "__main__":
    # Example usage
    pdf_path = input("Enter the path to your credit report PDF: ")
    try:
        dispute_letter = analyze_credit_report(pdf_path)
        print("\nGenerated Dispute Letter:")
        print(dispute_letter)
    except Exception as e:
        print(f"\nError: {str(e)}")