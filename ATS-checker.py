import os
import docx
from pdfminer.high_level import extract_text

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract text from resumes
def extract_resume_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    return ""

# Get all resumes from the folder
resumes_folder = "resumes/"
resumes = [os.path.join(resumes_folder, f) for f in os.listdir(resumes_folder) if f.endswith((".pdf", ".docx"))]

if resumes:
    for index, file_path in enumerate(resumes, start=1):
        text = extract_resume_text(file_path)
        print(f"Resume {index}: {os.path.basename(file_path)}")
        print(f"Raw Text:\n{text}")
        print("\n" + "-" * 80 + "\n")
else:
    print("No resumes found in the folder.")
