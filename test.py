import spacy

nlp = spacy.load("en_ushmm_rules")
doc = nlp("Auschwitz is a camp.")

for ent in doc.ents:
    print (ent.text, ent.label_)
