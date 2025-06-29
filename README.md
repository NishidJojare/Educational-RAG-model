# 🧠 RAG-Based Chatbot using FastAPI, LangChain & Groq AI

A lightweight Retrieval-Augmented Generation (RAG) chatbot built using **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Groq's llama3-70b-8192 model**, served with **FastAPI** and a beautiful frontend chat interface.


## 🚀 Features

- 🔎 Document-based intelligent Q&A
- 📚 PDF ingestion, chunking, and vector storage via FAISS
- 💬 Markdown-formatted LLM responses
- 🔗 Uses Groq’s blazing fast llama3-70b-8192 model
- 🗂️ Chat history is saved to a local file (`history.txt`)
- 🖥️ Frontend chat window with Bootstrap & Markdown rendering



## 🧰 Tech Stack

| Tool                | Purpose                                        |
|---------------------|------------------------------------------------|
| FastAPI             | Backend API Framework                          |
| LangChain           | RAG & chain management                         |
| FAISS               | Vector DB for document search                  |
| HuggingFace         | Sentence embeddings (model = all-MiniLM-L6-v2) |
| Groq                | llama3-70b-8192 LLM inference                  |
| Jinja2 + HTML/CSS   | Frontend chat UI                               |
| Markdown (marked.js)| Response rendering                             |



## ⚙️ Installation Guide


### 1️. Clone the Repository
```bash
git clone https://github.com/NishidJojare/Educational-RAG-model.git
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Get Groq API key
Visit to below page, create your own API key and save it in .env file. 

([https://console.groq.com/home](https://console.groq.com/home))

### 4. Prepare Document Embeddings
```
python create_embeddings.py
```

### 5. Start the Chatbot Server
```
fastapi dev main.py
```

### 6. Visit the webpage
([http://127.0.0.1:8000/](http://127.0.0.1:8000/))



## ☁️ Conversation Logs/History
It will be stored locally in
```
history.txt
```
