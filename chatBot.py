from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import asyncio

# Streamlit UI
st.title("Hi I'm Kiruba. This is my AI Chat Bot to assist you 🤖")

# Cache the Ollama model and chain setup to avoid reinitialization
@st.cache_resource
def load_chain():
    # Define Prompt Template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an AI assistant. Your name is KiruBot."),
            ("user", "Your query: {query}")
        ]
    )
    # Initialize Ollama model
    llm = Ollama(model="phi3")
    # Initialize output parser
    output_parser = StrOutputParser()
    # Create the chain
    chain = prompt | llm | output_parser
    return chain

# Load the chain
chain = load_chain()

# User input
user_input_txt = st.text_input("Please enter your queries here...")

# Asynchronous function to generate response
async def generate_response(query):
    return chain.invoke({"query": query})

# Generate and display response
if user_input_txt:
    with st.spinner("KiruBot is thinking..."):
        # Run the async function to generate the response
        response = asyncio.run(generate_response(user_input_txt))
    st.write(response)