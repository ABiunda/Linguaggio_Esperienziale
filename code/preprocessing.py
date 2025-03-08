import spacy

nlp = spacy.load("it_core_news_sm")

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return " ".join(tokens)

if __name__ == "__main__":
    testo = "Il dolore è inciso nel mio respiro, non posso negarlo."
    print(preprocess_text(testo))
