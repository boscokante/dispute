import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def step_a_identify_detailed_errors(pdf_text: str) -> str:
    """
    Step A: Identify an exhaustive list of errors from the credit report.
    """
    system_prompt = "You are a thorough credit report analyst."
    
    user_prompt = f"""
    I have the following PDF text from a credit report with a single negative tradeline. 
    I want you to identify every possible error, omission, or inconsistency in thorough detail.
    DO NOT summarize and DO NOT write a dispute letter yet. 
    Instead, list each category of errors carefully, referencing specific data in the PDF.

    Use the following checklist, and add more categories if you see relevant issues:
    1. Charge-Off Status vs. Available Credit
    2. Balance Consistency Over Time
    3. Scheduled/Actual Payment Data
    4. Amount Past Due Over Time
    5. Payment History Inconsistencies 
    6. Credit Limit vs. Negative Available Credit
    7. Charge-Off Amount vs. Balance
    8. Dates of First Delinquency and Closure
    9. Missing Account Details (e.g., Date of Last Activity, High Credit, Term Duration)
    10. Months Reviewed
    11. Creditor Classification
    12. Additional Comments/Discrepancies

    FORMAT:
    - Numbered or bullet-pointed list
    - Each point should have "Error:" or "Discrepancy:" lines 
      referencing exact or approximate text from the PDF.
    - Provide as many details as possible. 
    - This is not a dispute letter, just the error analysis.

    PDF TEXT:
    {pdf_text}
    """

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0,
        max_tokens=3000
    )
    return response.choices[0].message.content

def step_b_format_final(detailed_errors: str) -> str:
    """
    Step B: Format the detailed errors into a final dispute letter.
    """
    system_prompt = "You are a thorough credit report analyst."
    
    user_prompt = f"""
    We have a detailed error list from a credit report. Please convert it into
    the exact final format shown in the 'desired_output_example' below.

    DETAILED ERRORS:
    {detailed_errors}

    Instructions:
    1. Use the numbering style:
       (1), (2), (3)...
         a. Error: ...
         i. question...
         ii. question...
    2. Indent exactly as in the example (with spaces).
    3. Do NOT use "Questions" headings—just use "i., ii." lines after "Error:".
    4. End with a "Requested Action" section.
    5. Add "Below Are Excerpts from Credit Report..." at the end if appropriate.
    6. Keep the content of 'detailed_errors', but rephrase as needed
       to match the final style.
    """

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0,
        max_tokens=3000
    )
    return response.choices[0].message.content
