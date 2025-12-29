import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text, sentence_count=3):
    sentences = sent_tokenize(text)

    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return summary[:sentence_count]

if __name__ == "__main__":
    pdf_path = "sample.pdf"

    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text(text)

    print("📌 ÖZET:\n")
    for sentence in summary:
        print("-", sentence)
