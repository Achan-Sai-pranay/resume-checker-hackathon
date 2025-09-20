import fitz  # PyMuPDF
import pdfplumber
import docx2txt
import os

def extract_text_from_pdf(filepath):
    """Extract text from PDF using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
    return text.strip()

def extract_text_from_docx(filepath):
    """Extract text from DOCX using docx2txt."""
    try:
        text = docx2txt.process(filepath)
        return text.strip()
    except Exception as e:
        print(f"Error reading DOCX {filepath}: {e}")
        return ""

def parse_resume(filepath):
    """Detect file type and extract text."""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext in [".docx", ".doc"]:
        return extract_text_from_docx(filepath)
    else:
        return "Unsupported file format"