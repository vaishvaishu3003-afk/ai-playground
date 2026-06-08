import streamlit as st

st.title("My AI Playground")

question = st.text_input("Ask me anything")

if question:
    st.write(f"You asked: {question}")


