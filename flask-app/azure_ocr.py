from dotenv import load_dotenv
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential
from docx import Document
from pyresparser import ResumeParser
import json

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configurar el cliente de Form Recognizer
endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
model_id = "model_1"

credential = AzureKeyCredential(key)
document_model_admin_client = DocumentModelAdministrationClient(endpoint, credential)

def ocr_analysis(doc_name):
    try:
        with open(doc_name, "rb") as fd:
            document = fd.read()
        
        document_analysis_client = DocumentAnalysisClient(
            endpoint=endpoint, credential=AzureKeyCredential(key))
        
        poller = document_analysis_client.begin_analyze_document ("prebuilt-read", document)
        result = poller.result()
        
        # Extract text from OCR result
        extracted_text = str(result.content)
        
        return {'status': 'success', 'extracted_text': extracted_text}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

import nltk
from nltk.corpus import stopwords
import re

# download stopwords if necessary
nltk.download('stopwords')

# define stopwords list
stop_words = set(stopwords.words('english', 'spanish'))

# define function to clean text
def clean_text(text):
    # convert to lowercase
    text = text.lower()
    # remove URLs
    text = re.sub(r'http\S+', '', text)
    # remove special characters, punctuation, and emojis
    text = re.sub(r'[^\w\s]','',text)
    # tokenize into words
    words = nltk.word_tokenize(text)
    # remove stopwords
    words = [word for word in words if word not in stop_words]
    # join the words back into a string
    cleaned_text = ' '.join(words)
    return cleaned_text

import spacy
from skill_keywords import skills_list

import spacy

def extract_skills(ocr_string):
    # Load the spaCy model
    nlp = spacy.load('en_core_web_sm')
    

    # Parse the text using spaCy
    doc = nlp(ocr_string)

    # Extract the skill keywords that are present in the text
    skills = []
    for token in doc:
        if token.text.lower() in skills_list:
            skills.append(token.text.lower())

    # Remove duplicate skills
    skills = list(set(skills))
    
    return skills

