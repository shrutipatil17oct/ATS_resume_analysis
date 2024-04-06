from param import Range
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdfmodel
from dotenv import load_dotenv
import json
import os


key_self = os.environ['API_KEY']='AIzaSyC_5zH8EY2CJEXZyfbbChLilVdOx5mw'

genai.configure(api_key= key_self)


# creating function to get response from gemini model

def get_model(input_prompt):
    model= genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)
    return response.text
    
    
# converting pdf to text using PyPDF2
    
def pdf_to_text(pdfdata):
    reader = pdfmodel.PdfReader(pdfdata)
    text = ''
    for page in range(len(reader.pages)):
        page =reader.pages[page]
        text+=str(page.extract_text())
    return text

# prompt template as an input to gemini model

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jobd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

st.title('ATS Resume Analysis')
st.text("Let's see how can we improve your resume")
jobd = st.text_area('Please provide Job Description')
pdfdata=st.file_uploader('Upload your resume',type ='pdf')

submit = st.button('Submit')

if submit:
    if pdfdata is not None:
        text = pdf_to_text(pdfdata)
        response = get_model(input_prompt)
        st.subheader(response)