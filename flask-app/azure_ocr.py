import json
from dotenv import load_dotenv
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential
from docx import Document
from pyresparser import ResumeParser

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Configurar el cliente de Form Recognizer
endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")
model_id = "model_1"

credential = AzureKeyCredential(key)
document_model_admin_client = DocumentModelAdministrationClient(endpoint, credential)

def ocr_analysis(doc_name):

    with open(doc_name, "rb") as fd:
        document = fd.read()
    
        document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key))
    
    poller = document_analysis_client.begin_analyze_document ("prebuilt-read", document)
    result = poller.result()
    
    # Save dictionary to JSON file
    with open(doc_name + '.json', 'w') as json_file:
        json.dump(result.to_dict(), json_file)
    
    # Load JSON file and extract content to text file
    with open(doc_name + '.json', 'r') as json_file:
        pdf = json.load(json_file)
    
    with open(doc_name + '.txt', 'w') as text_file:
        # Write the contents of the dictionary to the text file
        text_file.write(str(pdf['content']))

    print ("OCR complete!!!")