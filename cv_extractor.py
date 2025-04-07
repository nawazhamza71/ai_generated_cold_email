import re
import fitz
import requests
import io

def extract_text_from_pdf(pdf_url):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        pdf_document = fitz.open(stream=io.BytesIO(response.content), filetype="pdf")
        text = "\n".join([page.get_text("text") for page in pdf_document])
        return text
    except Exception as e:
        print(f"Error extracting CV: {e}")
        return None