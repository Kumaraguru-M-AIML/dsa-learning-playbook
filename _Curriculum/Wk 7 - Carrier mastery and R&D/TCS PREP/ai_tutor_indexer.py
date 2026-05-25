import os
import argparse
import json

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False
    print("Warning: PyMuPDF not installed. PDF parsing will be skipped. Run: pip install PyMuPDF")

def process_pdf(file_path):
    if not HAS_FITZ:
        return {"error": "PyMuPDF not installed."}
    try:
        doc = fitz.open(file_path)
        toc = doc.get_toc()
        metadata = doc.metadata
        
        # Extract a preview of the first page (to understand what the doc is about)
        preview = ""
        if len(doc) > 0:
            preview = doc[0].get_text("text")[:500].replace('\n', ' ').strip()
            
        return {
            "type": "PDF",
            "pages": len(doc),
            "title": metadata.get("title", ""),
            "author": metadata.get("author", ""),
            "toc": toc, # List of [level, title, page_number]
            "preview": preview
        }
    except Exception as e:
        return {"error": str(e)}

def generate_folder_syllabus(folder_path):
    """Scans the folder and creates a localized syllabus markdown."""
    syllabus_path = os.path.join(folder_path, "_AI_MASTER_SYLLABUS.md")
    
    with open(syllabus_path, 'w', encoding='utf-8') as f:
        f.write("# AI Master Syllabus & Folder Index\n\n")
        f.write(f"**Target Folder:** `{folder_path}`\n")
        f.write("> *This file acts as a lightweight index for the AI to understand folder contents without burning tokens.*\n\n")
        
        for root, _, files in os.walk(folder_path):
            for file in files:
                ext = file.lower().split('.')[-1]
                if ext not in ['pdf', 'txt', 'md']:
                    continue
                    
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder_path)
                
                f.write(f"## File: `{rel_path}`\n")
                
                if ext == 'pdf':
                    data = process_pdf(file_path)
                    if "error" in data:
                        f.write(f"- *Error parsing PDF: {data['error']}*\n\n")
                        continue
                        
                    f.write(f"- **Pages:** {data['pages']}\n")
                    f.write(f"- **Preview:** *{data['preview']}...*\n\n")
                    
                    if data['toc']:
                        f.write("### Table of Contents\n")
                        # Only show top-level or level-2 TOC to save tokens
                        for item in data['toc']:
                            lvl, title, page = item
                            if lvl <= 2:
                                indent = "  " * (lvl - 1)
                                f.write(f"{indent}- Page {page}: {title}\n")
                    f.write("\n---\n\n")
                    
                elif ext in ['txt', 'md']:
                    # For text files, just grab the first 500 characters
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as tf:
                        preview = tf.read(500).replace('\n', ' ')
                    f.write(f"- **Type:** Text/Markdown\n")
                    f.write(f"- **Preview:** *{preview}...*\n\n")
                    f.write("---\n\n")

    print(f"✅ Success! Syllabus generated at: {syllabus_path}")
    return syllabus_path

def extract_pages(pdf_path, start_page, end_page):
    """Extracts specific pages from a PDF for precise token usage."""
    if not HAS_FITZ:
        print("Error: PyMuPDF not installed.")
        return
    
    try:
        doc = fitz.open(pdf_path)
        # fitz is 0-indexed, user inputs are usually 1-indexed
        start_idx = max(0, start_page - 1)
        end_idx = min(len(doc) - 1, end_page - 1)
        
        print(f"\n--- EXTRACTED CONTENT FROM {os.path.basename(pdf_path)} (Pages {start_page} to {end_page}) ---\n")
        for i in range(start_idx, end_idx + 1):
            page_text = doc[i].get_text("text")
            print(page_text)
            print(f"\n[--- End of Page {i+1} ---]\n")
            
    except Exception as e:
        print(f"Error extracting pages: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Optimized Folder & File Processor")
    parser.add_argument("--index", type=str, help="Path to folder to index")
    parser.add_argument("--fetch", type=str, help="Path to PDF file to extract from")
    parser.add_argument("--start", type=int, help="Start page (1-indexed)")
    parser.add_argument("--end", type=int, help="End page (inclusive)")
    
    args = parser.parse_args()
    
    if args.index:
        generate_folder_syllabus(args.index)
    elif args.fetch and args.start and args.end:
        extract_pages(args.fetch, args.start, args.end)
    else:
        print("Invalid arguments. Use --index <folder_path> OR --fetch <file> --start <p1> --end <p2>")
