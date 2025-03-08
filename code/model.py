from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-base-italian-uncased")
model = BertForSequenceClassification.from_pretrained("dbmdz/bert-base-italian-uncased", num_labels=3)

def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    output = model(**inputs)
    prediction = torch.argmax(output.logits, dim=1).item()
    categories = ["Esperienziale", "Astratto", "Strutturale"]
    return categories[prediction]

if __name__ == "__main__":
    testo = "Il dolore è inciso nel mio respiro, non posso negarlo."
    print("Categoria:", classify_text(testo))
