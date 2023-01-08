'''
The default model for the English language is designated as en_core_web_sm. 
'''
import sys
import spacy
print(sys.executable)
nlp = spacy.load("en_core_web_sm")
print(nlp)