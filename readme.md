# Credit Report Dispute Analyzer

This program analyzes credit report PDFs to help identify potential errors and generate dispute letters.

## Features

- PDF text extraction and processing
- Credit report error analysis using GPT
- Detailed error identification
- Formatted output for dispute letters

## Prerequisites

- Python 3.9+
- OpenAI API key
- PDF files to analyze

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dispute.git
cd dispute
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Create a `.env` file in the root directory
- Add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## Project Structure

```
dispute/
├── requirements.txt    # Project dependencies
├── src/
│   ├── __init__.py
│   ├── config.py      # Configuration and environment variables
│   ├── gpt_analyzer.py # GPT analysis functions
│   ├── main.py        # Main program entry point
│   └── pdf_processor.py # PDF processing functions
└── .env               # Environment variables (create this file)
```

## Usage

Run the program from the project root:
```bash
python src/main.py
```

## Dependencies

Main dependencies include:
- openai
- python-dotenv
- pdfplumber
- Other dependencies listed in requirements.txt

## Support

For issues or questions, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.