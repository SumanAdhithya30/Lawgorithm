# import os
# from pdfminer.high_level import extract_text
# from transformers import pipeline

# def extract_pdf_text(pdf_path):
#     """Extract text from the given PDF file."""
#     if not os.path.exists(pdf_path):
#         raise FileNotFoundError(f"{pdf_path} not found!")
#     return extract_text(pdf_path)

# def summarize_text(text, summarizer, max_length=100, min_length=30):
#     """
#     Summarize the provided text using the given summarizer pipeline.
#     Adjust max_length and min_length to produce a concise summary for winnability prediction.
#     """
#     # If text is very long, take a subset (you can customize this as needed)
#     text_to_summarize = text if len(text) < 1000 else text[:1000]
#     summary = summarizer(text_to_summarize, max_length=max_length, min_length=min_length, do_sample=False)
#     return summary[0]['summary_text']

# if __name__ == '__main__':
#     pdf_path = "/Users/batcomputer/Desktop/LAWGORITHMS/case_file.pdf"  # Replace with the path to your PDF file
#     full_text = extract_pdf_text(pdf_path)
    
#     # Initialize the summarization pipeline with a model suitable for summarization
#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
#     # Generate a concise summary for prediction input
#     summary_text = summarize_text(full_text, summarizer, max_length=100, min_length=30)
    
#     print("Concise Summary for Winnability Prediction:")
#     print(summary_text)
import os
import requests
import openai

# Set your API keys
openai.api_key = "YOUR_OPENAI_API_KEY"
API2CONVERT_API_KEY = "YOUR_API2CONVERT_API_KEY"

# API2Convert endpoint for converting PDF to text
API2CONVERT_URL = "https://v2.api2convert.com/convert/pdf/to/text"  # adjust if needed

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF using the API2Convert service."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found!")
    
    with open(pdf_path, "rb") as f:
        files = {"file": f}
        # Some APIs require the API key in headers; adjust if your service uses a different method.
        headers = {"Authorization": f"Bearer {API2CONVERT_API_KEY}"}
        response = requests.post(API2CONVERT_URL, files=files, headers=headers)
        
    if response.status_code != 200:
        raise Exception(f"API2Convert error: {response.status_code} - {response.text}")
    
    data = response.json()
    # Assume the API returns the extracted text under the "text" key.
    extracted_text = data.get("text", "")
    return extracted_text

def summarize_text_with_openai(text, max_tokens=150):
    """Generate a concise summary using OpenAI's API."""
    prompt = (
        "Summarize the following legal case details concisely, "
        "highlighting key factors for predicting case winnability:\n\n" + text
    )
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    summary = response.choices[0].text.strip()
    return summary

if __name__ == "__main__":
    pdf_path = "/Users/batcomputer/Desktop/LAWGORITHMS/case_file.pdf"  # Replace with the path to your PDF file
    print("Extracting text from PDF using API2Convert...")
    extracted_text = extract_text_from_pdf(pdf_path)
    print("Extracted text length:", len(extracted_text))
    
    print("Generating summary using OpenAI...")
    summary = summarize_text_with_openai(extracted_text)
    print("\nConcise Summary for Winnability Prediction:")
    print(summary)
