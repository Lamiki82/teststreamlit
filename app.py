import spacy
import streamlit as st 
from spacy_streamlit import visualize_ner


nlp = spacy.load('en_core_web_sm')
sampletext= st.text_input('inserire testo')
doc= nlp(sampletext)

if st.button('make NER'):
    visualize_ner(doc,labels=nlp.get_pipe('ner').labels)
