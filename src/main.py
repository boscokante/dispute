from pdf_processor import extract_text_from_pdf, extract_report_date
from prompt_manager import step_a_identify_detailed_errors, step_b_format_final
import os
import glob
from datetime import datetime

def main():
    # Sample account details - you would get these from the credit report
    account_details = {
        "bank_name": "BARCLAYS BANK DELAWARE",
        "address": "PO Box 8803, Wilmington, DE 19899-8803",
        "phone": "(888) 232-0780",
        "account_number": "Barclays xxxxxxxx 5205"
    }
    
    # You would get these from user input or the report
    name = "John Smith"
    report_number = "USER TO PROVIDE"
    
    try:
        # Find all PDFs in the reports directory
        pdf_files = glob.glob("reports/*.pdf")
        
        if not pdf_files:
            raise Exception("No PDF files found in the reports directory")
            
        pdf_path = pdf_files[0]
        print(f"Using PDF file: {pdf_path}")
        
        # Get text from PDF
        report_text = extract_text_from_pdf(pdf_path)
        
        # Extract report date
        date = extract_report_date(report_text)
        if not date:
            date = datetime.now().strftime("%m/%d/%Y")
            print("Warning: Could not extract report date, using current date")
        print(f"Report date: {date}")
        
        # Step A: Get detailed error analysis
        print("Analyzing report for errors...")
        detailed_errors = step_a_identify_detailed_errors(report_text)
        
        # Step B: Generate formatted dispute letter
        print("Generating formatted dispute letter...")
        dispute_letter = step_b_format_final(detailed_errors, account_details)
        
        # Create output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)
        
        # Save both the detailed analysis and final letter
        with open("output/detailed_errors.txt", "w") as f:
            f.write(detailed_errors)
        
        with open("output/dispute_letter.txt", "w") as f:
            f.write(dispute_letter)
            
        print("\nAnalysis saved to: output/detailed_errors.txt")
        print("Letter saved to: output/dispute_letter.txt")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()