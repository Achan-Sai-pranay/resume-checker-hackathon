from utils.parser import extract_text

# Change this path to match your test file
file_path = "../sample_resume.docx"   # or "../sample_resume.pdf"

try:
    text = extract_text(file_path)
    print("✅ Extracted Resume Text:")
    print(text[:500])  # print only first 500 chars
except Exception as e:
    print("❌ Error:", e)
