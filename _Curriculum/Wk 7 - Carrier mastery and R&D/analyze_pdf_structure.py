import pdfplumber
import sys

def analyze_structure(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        analysis = []
        for i, page in enumerate(pdf.pages):
            # Get text with layout to see columns
            text = page.extract_text(layout=True)
            analysis.append(f"--- PAGE {i+1} ---\n{text[:2000]}")
            
            # Look for font information if possible
            objects = page.chars
            if objects:
                fonts = set(obj.get('fontname', 'Unknown') for obj in objects[:100])
                sizes = set(obj.get('size', 0) for obj in objects[:100])
                analysis.append(f"Fonts detected: {fonts}")
                analysis.append(f"Sizes detected: {sizes}")
                
    return "\n".join(analysis)

if __name__ == "__main__":
    path = r"e:\Wk 7 - Carrier mastery and R&D\Career_Mastery_Hub\04_Experience_and_Projects\College_Projects\Decentralized_Social_Media_Project\Conferenece paper\D.A.S.T   the conference papr done by somebody , let us consider this as refernece.pdf"
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        print(analyze_structure(path))
    except Exception as e:
        print(f"Error: {e}")
