import pdfplumber
import sys

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    path = r"e:\Wk 7 - Carrier mastery and R&D\Career_Mastery_Hub\04_Experience_and_Projects\College_Projects\Decentralized_Social_Media_Project\Conferenece paper\Decentralized Social Media Platform with Content Authenticity Check data.pdf"
    try:
        content = extract_text(path)
        sys.stdout.reconfigure(encoding='utf-8')
        print(content[:5000]) # First 5000 chars
    except Exception as e:
        print(f"Error: {e}")
