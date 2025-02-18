from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# Streamlit UI
st.title("Hi I'm Kiruba. This is my AI Chat Bot to assist you 🤖")

user_input_txt = st.text_input("Please enter your queries here...")

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a AI assistant. Your name is KiruBot"),
        ("user", "your query: {query}")
    ]
)

llm = Ollama(model="phi3")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if user_input_txt:
    st.write(chain.invoke({"query": user_input_txt}))
