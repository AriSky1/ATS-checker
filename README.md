# ATS-checker

**ATS-checker** is a simple script designed to help job seekers and resume writers analyze the raw textual content extracted from resumes (PDF and DOCX formats). This content is what an **Applicant Tracking System (ATS)** typically sees when parsing your resume—before any recruiter ever does.

---

## 🔍 What It Does

- Scans a folder of resumes (PDF or DOCX)
- Extracts and prints the **raw text content** from each file
- Helps you preview how well your resume is **ATS-readable**

It uses:
- `pdfminer` for PDF text extraction
- `python-docx` for DOCX parsing

---

## 📂 Why It's Useful

Most modern companies use ATS software to screen candidates before human eyes ever see the resume. If your resume has too many graphics, columns, or unusual formatting, there's a risk the ATS will **misinterpret or skip key information**—like your experience or skills.

With **ATS-checker**, you can:

- Quickly validate if your resume is readable by ATS systems
- See what keywords and sections might be missing
- Debug formatting issues by inspecting what the ATS actually "reads"

---

## 🛠 How to Use

1. Place your resumes inside a folder named `resumes/` in the root directory of the project.
2. Run the Python script.
3. View raw extracted text from each resume in your terminal.

### Example Output

