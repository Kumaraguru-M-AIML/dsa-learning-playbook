import pdfplumber
import os
import sys

def full_scan(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    all_text = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total pages to scan: {total_pages}")
        
        for i, page in enumerate(pdf.pages):
            page_num = i + 1
            print(f"Scanning page {page_num}...")
            
            # Extract text
            text = page.extract_text()
            all_text.append(f"## PAGE {page_num}\n\n{text}\n\n---\n")
            
            # Save page image for visual scan
            img = page.to_image(resolution=150)
            img_path = os.path.join(output_dir, f"dast_page_{page_num}.png")
            img.save(img_path)
    
    # Save all text to a single report
    report_path = os.path.join(output_dir, "DAST_Full_Scan_Report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# D.A.S.T Full Scan Report\n\n")
        f.write("".join(all_text))
        
    print(f"Full scan complete. Report saved to {report_path}")

if __name__ == "__main__":
    pdf_file = r"e:\Wk 7 - Carrier mastery and R&D\Career_Mastery_Hub\04_Experience_and_Projects\College_Projects\Decentralized_Social_Media_Project\Conferenece paper\D.A.S.T   the conference papr done by somebody , let us consider this as refernece.pdf"
    out_dir = r"e:\Wk 7 - Carrier mastery and R&D\Career_Mastery_Hub\04_Experience_and_Projects\College_Projects\Decentralized_Social_Media_Project\Conferenece paper\DAST_Scan_Results"
    
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        full_scan(pdf_file, out_dir)
    except Exception as e:
        print(f"Error: {e}")
