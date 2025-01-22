from typing import Dict
import openai

def step_a_identify_detailed_errors(pdf_text: str) -> str:
    """
    Step A: Force GPT to identify an exhaustive list of errors, without summarizing or writing a final dispute letter.
    """
    system_prompt = """You are a thorough credit report analyst. Important rules:
    - Data is only required for 30 days prior to report date
    - Current month data is not required
    - Missing future data is never an error
    - Missing required data IS an error and must be noted
    - Normal reporting patterns are NOT errors:
        * Accounts can be simultaneously closed and charged-off
        * Charge-offs can occur at any time
        * Reporting continues after closure or charge-off
        * Reporting continues for 7 years after first delinquency
        * Closed accounts maintain their balance reporting"""
    
    user_prompt = f"""
    I have the following PDF text from a credit report with a single negative tradeline. 
    I want you to identify every possible error, omission, or inconsistency in thorough detail.
    DO NOT summarize and DO NOT write a dispute letter yet. 
    Instead, list each category of errors carefully, referencing specific data in the PDF.

    IMPORTANT RULES:
    - Document all missing required data fields
    - Note any inconsistencies created by missing data
    - Always specify months in date ranges (e.g., "Aug 2024 through Dec 2024")
    - Only consider data required for 30 days before report date
    - Example: For a report dated Jan 19, 2025, data must be present through Dec 2024
    - Charge-off timing is only an error if it conflicts with other reported data

    Use the following checklist, and add more categories if you see relevant issues:
    1. Charge-Off Status vs. Available Credit
    2. Balance Consistency Over Time (within required date range)
    3. Scheduled/Actual Payment Data
    4. Amount Past Due Over Time
    5. Payment History Inconsistencies 
    6. Credit Limit vs. Negative Available Credit
    7. Charge-Off Amount vs. Balance
    8. Dates of First Delinquency and Closure (only if contradicting other data)
    9. Missing Required Account Details
    10. Months Reviewed (within required date range)
    11. Creditor Classification
    12. Additional Comments/Discrepancies

    FORMAT:
    - Numbered list
    - Each point should have "Error:" lines 
    - For missing data that creates inconsistency, note both the missing data and the inconsistency
    - Provide specific references to the PDF text
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
        temperature=0.0
    )
    return response.choices[0].message.content

def step_b_format_final(detailed_errors: str, account_details: Dict) -> str:
    """
    Step B: Transform detailed errors into formatted dispute document
    """
    system_prompt = """You are a precise credit report analyst. Your responses should be:
    - Clinical and factual
    - Document missing data points
    - Question specific contradictions, not theoretical possibilities
    - Focus on what happened in this specific case"""
    
    user_prompt = f"""
    Transform these detailed errors into a structured dispute document. Format each issue as follows:

    1. [Technical Category]
        a. Error: [Specific factual description, including any missing data]
        i. [Direct question about what happened in this specific case]
        ii. [Follow-up question about specific contradiction]

    Required format:
    - Start immediately with numbered issues
    - Each error must reference exact data points
    - For missing data:
        * State what is missing and when
        * If missing data creates contradiction, ask about the contradiction
        * If no contradiction, simply note the missing data
    - Questions must:
        * Be specific to this account
        * Ask what happened, not what's possible
        * Focus on actual contradictions
        * Reference specific dates and amounts
    - End with "Requested Action: Please verify and address all identified discrepancies"
    - Include relevant account details at bottom

    Example questions:
    ❌ "Is it possible for the past due amount to exceed the charge-off amount?"
    ✅ "How did the past due amount reach $5,000 when the charge-off amount is listed as $3,500?"
    ❌ "Could an account have payments after charge-off?"
    ✅ "Why does the payment history show $200 paid in March 2024 when the account was charged-off in January 2024?"

    Account Information:
    Bank: {account_details['bank_name']}
    Address: {account_details['address']}
    Phone: {account_details['phone']}
    Account: {account_details['account_number']}

    DETAILED ERRORS:
    {detailed_errors}
    """

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0
    )
    return response.choices[0].message.content 