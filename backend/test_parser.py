import os
from parser import parse_resume

# Base directory (where this script is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to your resume file
resume_file = os.path.join(BASE_DIR, "sample_resumes", "functionalsample.pdf")

# Check if file exists
if not os.path.exists(resume_file):
    print(f"❌ File not found: {resume_file}")
    exit()

print("=" * 50)
print(f"📄 Testing file: {resume_file}")

text = parse_resume(resume_file)

if text:
    print(f"✅ Extracted text (first 500 chars):\n{text[:500]}")
else:
    print("⚠️ No text extracted") 
