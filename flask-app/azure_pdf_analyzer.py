"""
This code sample shows Prebuilt Read operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from flask import json

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://curri-ofertas.cognitiveservices.azure.com/"
key = "49c2cbd1ee6b4f9e85a6b413b939109c"


def analyze_read():
    # sample document
    formUrl = "https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/cv-app/raw/dev/cv_prueba_full_stack.pdf "

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
    poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", formUrl)
    result = poller.result()

    print ("Document contains content: ", result.content)
    
    for page in result.pages:
        print("----Analyzing Read from page #{}----".format(page.page_number))
        print(
            "Page has width: {} and height: {}, measured with unit: {}".format(
                page.width, page.height, page.unit
            )
        )

        
        
        
        for word in page.words:
            print(
                "{}".format(
                    word.content
                )
            )

            json_data = {
                    "text": word.content,
                    
                }
            pretty_json = json.dumps(json_data, indent=4)

    print(pretty_json)
        


    

    print("----------------------------------------")

    




if __name__ == "__main__":
    analyze_read()
