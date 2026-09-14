# 🧠 DocuMind AI

> An AI-powered document intelligence system that lets users upload documents, search them semantically, and ask natural-language questions using Retrieval-Augmented Generation (RAG).

DocuMind AI is a full-stack application designed to extract, understand, retrieve, and analyze information from unstructured documents such as **PDF, DOCX, TXT, and EML files**.

Instead of manually searching through large documents, users can simply ask questions in natural language and get relevant, context-aware answers.

---

## 🚀 Features

- 📄 Upload PDF, DOCX, TXT, and EML documents
- 🔍 Semantic search across uploaded documents
- 🤖 AI-powered question answering using RAG
- 🧩 Automatic document chunking
- 🧠 Sentence Transformer embeddings
- ⚡ FAISS-based vector similarity search
- 💬 Natural-language AI chat interface
- 📚 Document library with processing status
- 📌 Source-aware retrieval using document/chunk metadata
- 🌐 Modern React-based web interface
- 🔌 REST APIs using FastAPI
- 🗄️ MongoDB for document metadata
- 🔐 API keys kept outside the source code using environment variables

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      React UI       │
                    │   Vite + Tailwind   │
                    └──────────┬──────────┘
                               │
                               │ HTTP / REST
                               ▼
                    ┌─────────────────────┐
                    │     FastAPI API     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌───────────┐    ┌────────────┐   ┌─────────────┐
        │ MongoDB   │    │   FAISS    │   │ Gemini API  │
        │ Metadata  │    │ Vector DB  │   │    LLM      │
        └───────────┘    └────────────┘   └─────────────┘
                               ▲
                               │
                    ┌──────────┴──────────┐
                    │ Document Processing │
                    │ Extraction + Chunk  │
                    │ + Embeddings        │
                    └─────────────────────┘