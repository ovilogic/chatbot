import spacy

nlp = spacy.load('en_core_web_md')
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc if w.tag_ == 'VBG' or w.tag_ == 'VB'])
print([w.text for w in doc if w.pos_ == 'PROPN'])