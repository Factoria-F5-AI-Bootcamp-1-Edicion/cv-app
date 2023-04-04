from werkzeug.utils import secure_filename
import os
import nltk
from pyresparser import ResumeParser
from docx import Document
from flask import Flask,render_template,redirect,request, url_for
import numpy as np
import pandas as pd
import re
from ftfy import fix_text
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential
from docx import Document
from azure_ocr import ocr_analysis, clean_text, extract_skills
import json

stopw  = set(stopwords.words('english','spanish'))

df =pd.read_csv('job_final.csv') 
df['test']=df['Job_Description'].apply(lambda x: ' '.join([word for word in str(x).split() if len(word)>2 and word not in (stopw)]))

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template("model.html")



@app.route("/home")
def home():
    return redirect('/')

@app.route('/submit',methods=['POST'])
def submit_data():
    if request.method == 'POST':

        f=request.files['userfile']
        f.save(f.filename)
        ocr = ocr_analysis(f.filename)
        ocr_string = json.dumps(ocr['extracted_text'])
        cleaned_text = clean_text(ocr_string)
        skills = extract_skills(cleaned_text)

        org_name_clean = skills
        
        def ngrams(string, n=3):
            string = fix_text(string) # fix text
            string = string.encode("ascii", errors="ignore").decode() #remove non ascii chars
            string = string.lower()
            chars_to_remove = [")","(",".","|","[","]","{","}","'"]
            rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
            string = re.sub(rx, '', string)
            string = string.replace('&', 'and')
            string = string.replace(',', ' ')
            string = string.replace('-', ' ')
            string = string.title() # normalise case - capital at start of each word
            string = re.sub(' +',' ',string).strip() # get rid of multiple spaces and replace with a single
            string = ' '+ string +' ' # pad names for ngrams...
            string = re.sub(r'[,-./]|\sBD',r'', string)
            ngrams = zip(*[string[i:] for i in range(n)])
            return [''.join(ngram) for ngram in ngrams]
        vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams, lowercase=False)
        tfidf = vectorizer.fit_transform(org_name_clean)
        print('Vecorizing completed...')
        
        
        def getNearestN(query):
          queryTFIDF_ = vectorizer.transform(query)
          distances, indices = nbrs.kneighbors(queryTFIDF_)
          return distances, indices
        nbrs = NearestNeighbors(n_neighbors=1, n_jobs=-1).fit(tfidf)
        unique_org = (df['test'].values)
        distances, indices = getNearestN(unique_org)
        unique_org = list(unique_org)
        matches = []
        for i,j in enumerate(indices):
            dist=round(distances[i][0],1)
  
            temp = [dist]
            matches.append(temp)
        matches = pd.DataFrame(matches, columns=['Match confidence'])
        
        from sklearn.preprocessing import MinMaxScaler

        # Invert the distances and then scale them to a 0-100% range
        scaler = MinMaxScaler(feature_range=(0, 100))
        matches['Match confidence'] = scaler.fit_transform(1 - matches[['Match confidence']])

        # Format the Match confidence column to include the % sign and show no decimal places
        matches['Match confidence'] = matches['Match confidence'].map('{:.0f}%'.format)
        df['match']=matches['Match confidence']
        df1=df.sort_values('match', ascending=False)

        df2=df1[['Position', 'Company', 'match','url']].head(10).reset_index()
        
        
        
        
        
    # return  'nothing' 
    return render_template('model.html',tables=[df2.to_html(classes='job')],titles=['na','Job'])
        
        
        
        
        
if __name__ =="__main__":
    
    app.run(debug=True, host='0.0.0.0')