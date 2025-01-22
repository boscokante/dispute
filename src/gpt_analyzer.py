from openai import OpenAI
from config import OPENAI_API_KEY

def format_dispute_letter(name, report_number, date, account_details, analysis_points):
    """
    Formats the dispute letter in a structured format with detailed points and sub-points.
    """
    letter = f"""Name: {name}

Report: {report_number}

Date: {date}

Account Name: {account_details.get('bank_name', 'N/A')}
Account Address: {account_details.get('address', 'N/A')}
Account Phone: {account_details.get('phone', 'N/A')}
Account number: {account_details.get('account_number', 'N/A')}

Summary: This document details errors and omissions in the {account_details.get('bank_name', '')} 
entry on my credit report. The account shows several inconsistencies and missing information 
that require clarification. Below is a structured list of these errors and omissions.

"""
    
    # Add analysis points with proper formatting
    for i, point in enumerate(analysis_points, 1):
        # Main point
        letter += f"\n{i}. {point['main_point']}\n"
        
        # Sub-points with a, b, c...
        for j, sub_point in enumerate(point.get('sub_points', []), 97):  # 97 is ASCII for 'a'
            letter += f"\n    {chr(j)}. Error: {sub_point['description']}\n"
            
            # Sub-sub-points with roman numerals
            for k, detail in enumerate(sub_point.get('details', []), 1):
                letter += f"\n        {to_roman(k)}. {detail}\n"
    
    return letter

def to_roman(num):
    """Convert integer to Roman numeral."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num.lower()

def analyze_credit_report(report_text):
    """
    Analyzes credit report text to identify issues and structure them in a detailed format.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    analysis_prompt = """
    Analyze this credit report section and identify issues in these categories:
    1. Status and Balance Inconsistencies
    2. Payment History Issues
    3. Credit Limit and Available Credit Discrepancies
    4. Dates and Timeline Issues
    5. Missing or Incomplete Information
    
    Format each issue with:
    - A clear main point
    - Specific sub-points describing each error
    - Detailed questions or clarifications needed
    
    Keep the technical accuracy of the current analysis but format it like a formal dispute letter.
    """
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": analysis_prompt},
            {"role": "user", "content": report_text}
        ]
    )
    
    analysis = parse_gpt_response(response.choices[0].message.content)
    return analysis

def parse_gpt_response(gpt_response):
    """
    Parses GPT response into structured format for the letter.
    Returns a list of dictionaries containing main points, sub-points, and details.
    """
    # Implementation of parsing logic
    # This would convert the GPT response into structured data
    # You would implement the actual parsing based on your GPT response format
    
    # Example structure:
    analysis_points = [
        {
            "main_point": "Balance and Status Inconsistencies",
            "sub_points": [
                {
                    "description": "The account is marked as \"Charge-Off,\" but shows contradictory available credit",
                    "details": [
                        "How can a charged-off account have available credit?",
                        "What is the significance of the negative available credit?"
                    ]
                }
            ]
        }
    ]
    
    return analysis_points

def generate_dispute_letter(report_text, name, report_number, date, account_details):
    """
    Main function to generate the complete dispute letter.
    """
    analysis_points = analyze_credit_report(report_text)
    return format_dispute_letter(name, report_number, date, account_details, analysis_points)