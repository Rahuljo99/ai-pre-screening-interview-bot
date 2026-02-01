import fitz # PyMuPDF

def resume_parser(file : bytes) -> str:
    try:
        doc = fitz.open(stream=file, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        doc.close()
    except Exception as e:
        print(f"Error parsing resume: {e}")
        raise ValueError("Failed to parse resume. Ensure the file is a valid PDF.")
    return text

