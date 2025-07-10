
# 🧠 RAG Chatbot (Streamlit + ChromaDB + Groq)

This project is a **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **LangChain**, **ChromaDB**, and **Groq**. It enables users to query a pre-loaded document (e.g., a PDF) and receive intelligent answers powered by Groq’s LLM. Users **do not upload** their own documents—the document is already processed and indexed in the backend.

---

## 🚀 Key Features (MVPs)

- ✅ Load and split a static PDF into text chunks
- ✅ Generate sentence embeddings using SentenceTransformer (`all-MiniLM-L6-v2`)
- ✅ Store and retrieve document vectors from **ChromaDB**
- ✅ Embed user queries and match them semantically with chunks
- ✅ Use **Groq LLM** (via LangChain) to respond to questions with retrieved context
- ✅ Real-time interactive **Streamlit chatbot UI**

---

## 🧠 High-Level System Architecture

```plaintext
        ┌─────────────┐
        │  .env File  │        ◄── GROQ API Key, Model Name
        └─────┬───────┘
              │
        ┌─────▼───────┐
        │ PDF Loader  │        ◄── PDF is loaded from /data/
        └─────┬───────┘
              │
        ┌─────▼────────────┐
        │ Text Splitter    │        ◄── RecursiveCharacterTextSplitter
        └─────┬────────────┘
              │
        ┌─────▼────────────┐
        │ Embedding Model  │        ◄── SentenceTransformer (MiniLM)
        └─────┬────────────┘
              │
        ┌─────▼────────────┐
        │  ChromaDB        │        ◄── Vector Store (document chunks)
        └─────┬────────────┘
              │
┌─────────────▼────────────┐
│   Streamlit Chatbot UI   │  ◄── Groq LLM fetches response based on query + context
└──────────────────────────┘
```

---

## 📁 Project Structure

```bash
├── chatbot_main.py         # Streamlit app: chatbot interface + Groq LLM
├── chroma_setup.py         # Handles loading PDF, chunking, embedding, and storing in ChromaDB
├── data/
│   └── the-seven-habits.pdf  # Preloaded PDF document
├── data_store/             # Persistent ChromaDB vector database
├── Dockerfile              # Docker config for Streamlit app
├── docker-compose.yml      # Orchestrates Streamlit app + ChromaDB
├── .env                    # API credentials (GROQ_API_KEY and GROQ_MODEL)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🐳 Docker Setup

### 1. Docker Compose File

```yaml
version: "3.9"
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8501:8501"
    env_file:
      - .env

  chroma:
    image: chromadb/chroma:latest
    volumes:
      - ./chroma_db:/data
    ports:
      - "8765:8000"
```

---

### 2. Dockerfile

```Dockerfile
# Streamlit app Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "chatbot_main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## ✅ How It Works

1. The backend loads a static PDF (`the-seven-habits.pdf`)
2. The text is split into smaller chunks
3. Each chunk is embedded into a vector using a sentence transformer model
4. The vectors are stored in ChromaDB
5. When a user sends a query:
   - The query is embedded
   - A similarity search retrieves relevant chunks
   - The Groq LLM is prompted with both the query and the relevant context

---

## 💡 Technologies Used

- **Streamlit** — UI for chat interactions
- **LangChain** — Framework for chaining LLM calls and managing messages
- **ChromaDB** — Vector store to store and retrieve document embeddings
- **SentenceTransformers** — Local embedding model (`all-MiniLM-L6-v2`)
- **Groq LLM (Llama 3)** — Used via LangChain’s `ChatGroq`

---

## 🌱 Future Improvements

- Allow document uploads by users (optional)
- Add citation sources from PDF in each answer
- Add feedback mechanism to rate answers
- Add PDF summarization feature
- Host on a public cloud (e.g., Hugging Face Spaces or Render)

---

## 🏁 Getting Started (Local)

```bash
git clone https://github.com/your-username/module-2.git
cd module-2

# Set up virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GROQ_API_KEY=your_key" > .env
echo "GROQ_MODEL=llama-3-8b" >> .env

# Run with Streamlit
streamlit run chatbot_main.py
```

---

## ✍️ Author

Built by [Your Byaruhanga Johnson]

