# 🧠 LangChain Chatbot using Streamlit & Groq

This is an interactive chatbot built with **Streamlit**, powered by **LangChain** and the **Groq API** using the `llama-3.1-8b-instant` model. It supports dynamic user interactions and retains conversation history using Streamlit's `session_state`.

---

## 🚀 Features

- 🤖 Chatbot interface using Streamlit
- 💬 Memory: Remembers previous messages during a session
- ⚡ Powered by Groq’s blazing fast LLM
- 🧱 Built with LangChain for structured messaging
- 🔐 Uses `.env` file to securely store API keys

---

## 📁 Project Structure

```bash
├── chatbot_main.py         # Main Streamlit application
├── .env                   # Environment variables (API keys and model name)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Inside the root directory, create a `.env` file and add your API key and model:

```env
GROQ_API_KEY="your_groq_api_key_here"
GROQ_MODEL="llama-3.1-8b-instant"
```

> 📝 You can get a Groq API key at https://console.groq.com/

---

### 5. Run the app

```bash
streamlit run chatbot_app.py
```

Then open your browser at the local address shown (e.g., http://localhost:8501).

---

## 📦 Example `requirements.txt`

```txt
streamlit
langchain-groq
python-dotenv
```

---

