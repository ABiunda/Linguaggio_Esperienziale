import streamlit as st
from model import classify_text

st.title("Classificatore di Testi Filosofici")

input_text = st.text_area("Inserisci un testo")

if st.button("Analizza"):
    categoria = classify_text(input_text)
    st.write("Categoria:", categoria)
