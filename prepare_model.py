import spacy
from spacy.language import Language

main_nlp = spacy.load("model-best")

@Language.component("align_entities")
def align_entities(doc):
    # ents = list(doc.ents)
    ents = []
    for ent in doc.ents:
        if ent.label_ == "GPE" or ent.label_ == "LOC":
            ent.label_ = "LOCATION"
        ents.append(ent)

    doc.ents = ents
    return (doc)

nlp = spacy.load("en_core_web_sm")

Language.component("align_entities", func=align_entities)

main_nlp.add_pipe("ner", source=nlp, name="ner_sm", after="ner")
# main_nlp.add_pipe("align_entities", after="ner_sm")
print (nlp.pipe_names)

nlp.to_disk("ushmm_sm_final")
