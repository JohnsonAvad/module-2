import streamlit as st
from dotenv import dotenv_values
from chroma_setup import setup_chroma_collection, embedding_function
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import numpy as np
from datetime import datetime

# Load ChromaDB Collection 
collection, _ = setup_chroma_collection("./data/the-seven-habits.pdf")

# Load Groq API Key & Model 
config = dotenv_values(".env")
groq_api_key = config["GROQ_API_KEY"]
groq_model = config["GROQ_MODEL"]

# Streamlit UI Setup 
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("🧠 RAG-Powered Chatbot (Chroma + Groq)")

today = datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
st.write(f"📅 Today is **{today}**")

# Initialize ChatGroq LLM object with 
# chosen model and key
# Checks if LLM is already stored in session
#  state to prevent reinitializing
#  on every rerun
if "llm" not in st.session_state:
    st.session_state.llm = ChatGroq(
        model=groq_model,
        api_key=groq_api_key,
        temperature=0.7
    )
    # 0.7 temp makes the output llm creative
    #  but focused
llm = st.session_state.llm

# System Prompt allows user to customize the 
# chatbot behaviour.
system_prompt = st.text_area("System Prompt", value="You are a helpful assistant. Use the retrieved document content to " \
"answer clearly and concisely. What you dont know say I dont know")

# Initialize Message History 
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=system_prompt)]

#  Display Chat History 
for message in st.session_state.messages:
    role = "user" if isinstance(message, HumanMessage) else "assistant" if isinstance(message, AIMessage) else "system"
    with st.chat_message(role):
        st.markdown(message.content)

#  Generate response with a RAG function
# Step1 is to embed the query
def generate_rag_response(query: str):
    query_embedding = np.array(embedding_function([query])[0])
    results = collection.query(query_embeddings=query_embedding, n_results=2)
    retrieved_docs = results["documents"][0]
    context = "\n\n".join(retrieved_docs)

    # Add context to the prompt
    context_prompt = f"Context:\n{context}\n\nQuestion:\n{query}"
    st.session_state.messages.append(HumanMessage(content=context_prompt))

    response = llm.invoke(st.session_state.messages)
    st.session_state.messages.append(response)
    return response

# User Input
if user_query := st.chat_input("Ask something from the document..."):
#    Call the rag function
    generate_rag_response(user_query)
    st.rerun()
