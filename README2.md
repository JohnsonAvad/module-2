# 🧠 PDF → Chunks → Embeddings → Chroma Pipeline

A simple pipeline that:
1. Loads a PDF document  
2. Splits it into token-based chunks  
3. Embeds each chunk using Azure OpenAI  
4. Stores the resulting vectors in a Chroma vector database  
5. Supports semantic search over the stored chunks

---

## 🚀 Prerequisites

- Python 3.9+  
- Azure OpenAI resource & key  
- Docker & Docker‑Compose (for Chroma container)  
- PDF placed in `./data/`

---

## ⚙️ Setup & Configuration

1. Add Azure credentials to a `.env` file  
2. (Optional) Run Chroma via Docker Compose

---

## 📁 Project Structure

