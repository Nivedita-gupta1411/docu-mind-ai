# 🧠 DocuMind AI

> An AI-powered document intelligence system that lets users upload documents, search them semantically, and ask natural-language questions using Retrieval-Augmented Generation (RAG).

DocuMind AI is a full-stack AI application designed to **extract, process, retrieve, and analyze information from unstructured documents** such as PDF, DOCX, TXT, and EML files.

Instead of manually searching through large documents, users can ask questions in natural language and receive context-aware answers grounded in their uploaded documents.

---

## 🚀 Live Demo

🌐 **[Try DocuMind AI](https://docu-mind-ai-yksm-sigma.vercel.app/)**

💻 **[View Source Code on GitHub](https://github.com/Nivedita-gupta1411/docu-mind-ai)**

> The frontend is deployed on Vercel and the backend is deployed on Render.

---

## ✨ Features

- 📄 Upload PDF, DOCX, TXT, and EML documents
- 🔍 Semantic search across uploaded documents
- 🤖 AI-powered question answering using RAG
- 🧩 Automatic document chunking with configurable overlap
- 🧠 Gemini Embeddings for semantic representation
- ⚡ FAISS-based vector similarity search
- 💬 Natural-language AI chat interface
- 📚 Document library with processing status
- 📌 Document and chunk metadata for source-aware retrieval
- 🌐 Modern React-based web interface
- 🔌 REST APIs using FastAPI
- 🗄️ MongoDB for document metadata
- 🔐 API keys managed securely through environment variables
- ☁️ Deployed frontend and backend

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      React UI        │
                         │   Vite + Tailwind    │
                         └──────────┬───────────┘
                                    │
                              HTTP / REST
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     FastAPI API      │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
          ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
          │   MongoDB   │    │    FAISS    │    │   Gemini    │
          │  Metadata   │    │ Vector Index│    │     LLM     │
          └─────────────┘    └──────▲──────┘    └──────▲──────┘
                                    │                  │
                                    │                  │
                              ┌─────┴──────┐     ┌─────┴──────┐
                              │   Gemini   │     │    RAG     │
                              │ Embeddings │     │  Pipeline  │
                              └─────▲──────┘     └─────▲──────┘
                                    │                  │
                                    └────────┬─────────┘
                                             │
                                  ┌──────────┴──────────┐
                                  │ Document Processing  │
                                  │                      │
                                  │ Extraction           │
                                  │ Chunking             │
                                  │ Embeddings           │
                                  └──────────────────────┘
🔄 RAG Pipeline

DocuMind AI uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions based on the user's uploaded documents.

The pipeline consists of:

Document Upload
      ↓
Text Extraction
      ↓
Document Chunking
      ↓
Gemini Embeddings
      ↓
FAISS Vector Store
      ↓
Semantic Retrieval
      ↓
Relevant Context
      ↓
Gemini LLM
      ↓
AI Generated Answer
1. 📤 Document Upload

Users can upload documents through the web interface.

Supported formats
PDF
DOCX
TXT
EML

The backend validates the uploaded file and processes it asynchronously.

2. 📑 Text Extraction

The backend extracts textual content from the uploaded document based on its file type.

The extracted text is then passed to the chunking stage.

3. 🧩 Document Chunking

Large documents are divided into smaller overlapping chunks before generating embeddings.

Current configuration
Chunk Size     : 700 words
Chunk Overlap  : 100 words

The overlap helps preserve contextual information between neighboring chunks.

For example:

Chunk 1
████████████████████████████████

                  ↓ 100-word overlap

             Chunk 2
             ████████████████████████████████
4. 🧠 Embeddings

Each document chunk is converted into a numerical vector representation using Gemini Embeddings.

Embedding Model
gemini-embedding-001
Embedding Dimension
768

The embedding represents the semantic meaning of the text and allows the system to compare documents based on meaning rather than exact keyword matches.

5. ⚡ Vector Storage

The generated embeddings are stored in a FAISS vector index.

FAISS enables efficient similarity-based retrieval of relevant document chunks.

The system also stores metadata associated with each chunk, including document information and chunk details.

6. 🔎 Semantic Retrieval

When the user asks a question, the query is converted into an embedding using the retrieval-query embedding configuration.

User Question
      ↓
Query Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks

The system retrieves the most relevant chunks based on vector similarity.

Default Retrieval Configuration
Top-K : 5
7. 🤖 LLM Generation

The retrieved document context is combined with the user's question and passed to the Gemini model.

Relevant Context
       +
User Question
       ↓
     Gemini
       ↓
AI Generated Answer

This allows the generated response to be grounded in information retrieved from the user's documents.

🧠 Why RAG?

A Large Language Model does not automatically have access to a user's private documents.

RAG solves this problem by retrieving relevant information from the document collection before generating an answer.

User Documents
      ↓
Document Processing
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Search
      ↓
Relevant Context
      ↓
LLM
      ↓
Context-Aware Answer

This approach allows the application to work with user-specific document knowledge without requiring the model to be trained on those documents.

🔍 Semantic Search

Traditional keyword search mainly looks for exact words.

Semantic search represents both the user's query and document chunks as embeddings and compares their semantic similarity.

Example

Query:

"software development experience"

The system can potentially retrieve a document section containing:

"Built scalable web applications using React and Node.js."

even when the exact query words do not appear in the document.

This makes semantic search more useful for natural-language document exploration.

🛠️ Tech Stack
Frontend
React
Vite
Tailwind CSS
Axios
JavaScript
Backend
Python
FastAPI
Uvicorn
Pydantic
AI / NLP
Google Gemini
Gemini Embeddings
Retrieval-Augmented Generation (RAG)
Semantic Search
Text Embeddings
Natural Language Processing
Vector Search
FAISS
NumPy
Database
MongoDB
Document Processing
PyPDF2
python-docx
Python email parsing
Development
Git
GitHub
VS Code
Deployment
Vercel — Frontend
Render — Backend
MongoDB Atlas — Database
📁 Project Structure
docu-mind-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   ├── documents.py
│   │   │   ├── search.py
│   │   │   └── upload.py
│   │   │
│   │   ├── services/
│   │   │   ├── document_processor.py
│   │   │   ├── embeddings.py
│   │   │   ├── retriever.py
│   │   │   ├── vector_store.py
│   │   │   ├── rag.py
│   │   │   └── llm.py
│   │   │
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── .env
│
├── data/
│   ├── uploads/
│   ├── processed/
│   └── vector_store/
│
├── .env.example
├── .gitignore
└── README.md
🔌 API Endpoints
Method	Endpoint	Description
POST	/api/upload	Upload and process a document
GET	/api/documents	Get uploaded documents
GET	/api/documents/{doc_id}	Get document details
DELETE	/api/documents/{doc_id}	Delete a document
POST	/api/search	Perform semantic search
POST	/api/chat	Ask questions using RAG
GET	/api/health	Check backend health
📖 Interactive API Documentation

FastAPI provides interactive Swagger documentation.

Local
http://localhost:8001/docs

The Swagger interface can be used to test the REST APIs directly.

⚙️ Environment Variables
Backend

Create:

backend/.env

Example:

MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=doc_intel

EMBEDDING_MODEL=gemini-embedding-001
EMBEDDING_DIMENSION=768

LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash

CHUNK_SIZE_WORDS=700
CHUNK_OVERLAP_WORDS=100

MAX_UPLOAD_SIZE_MB=50
TOP_K=5
Frontend

Create:

frontend/.env

For local development:

VITE_API_BASE_URL=http://localhost:8001/api

For the deployed frontend, the API base URL points to the deployed Render backend.

⚠️ Never commit real API keys, database credentials, or other secrets to GitHub.

💻 Local Setup
1. Clone the Repository
git clone https://github.com/Nivedita-gupta1411/docu-mind-ai.git

cd docu-mind-ai
2. Backend Setup

Navigate to the backend:

cd backend

Create a virtual environment:

python -m venv venv
Windows
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create the .env file and configure the required environment variables.

Start the FastAPI server:

uvicorn app.main:app --reload --port 8001

Backend:

http://localhost:8001

Swagger:

http://localhost:8001/docs
🎨 Frontend Setup

Open another terminal:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

Frontend:

http://localhost:5173
🧪 Example Usage
Upload a Document

Upload a document such as:

resume.pdf

The system processes it through:

Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Gemini Embeddings
   ↓
FAISS Index
Ask Questions

After the document has been processed, users can ask questions such as:

What technologies are mentioned in my resume?

Explain my AI document project.

What projects have I worked on?

What interview questions can be asked about my projects?

The system retrieves relevant document chunks and provides them as context to Gemini before generating the final response.

🎯 Use Cases
🎓 Students

Upload:

Lecture notes
Study material
Assignments
Research papers

and ask questions directly using natural language.

👨‍💻 Developers

Upload:

Technical documentation
Project documentation
API documentation

and search through them using semantic search.

📄 Resume Analysis

Upload a resume and ask questions about:

Skills
Projects
Experience
Technical knowledge
Potential interview questions
🏢 Business Documents

Organizations can use document intelligence systems to search and analyze large collections of internal documents.

📚 Research

Researchers can retrieve relevant information from large document collections without manually searching through every document.

🔒 Security

Sensitive credentials are managed through environment variables.

The following should never be committed to GitHub:

.env
API keys
Database credentials
Uploaded documents
Processed documents
Generated vector indexes

These files are excluded using .gitignore.

📈 Current Limitations

The current implementation intentionally keeps the architecture lightweight.

Chat history is not permanently persisted.
FAISS/vector data is stored locally.
Uploaded and processed files are stored locally.
Authentication is not implemented.
No reranking model is currently used.
Production-scale persistent storage is not implemented for vector indexes and uploaded files.
Render's local filesystem can be reset during service restarts or redeployments.
🚀 Future Improvements

Potential improvements include:

🔐 User authentication and authorization
💬 Persistent conversation history
☁️ Cloud-based document storage
🗄️ Production-ready vector database
🎯 Retrieval reranking
📊 Retrieval and answer evaluation
🌍 Multi-language document support
📑 Improved page-level source citations
🧠 Conversation-aware retrieval
⚡ Streaming LLM responses
📈 Usage analytics
🐳 Docker-based deployment
📈 Scalable production infrastructure
🔄 Complete Project Pipeline
                 DOCUMENT INTELLIGENCE PIPELINE

                         ┌──────────────┐
                         │   Document   │
                         └──────┬───────┘
                                │
                                ▼
                       ┌────────────────┐
                       │ Text Extraction│
                       └───────┬────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │    Chunking    │
                       │    700 / 100   │
                       └───────┬────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │ Gemini         │
                       │ Embeddings     │
                       │ 768 dimensions │
                       └───────┬────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │     FAISS      │
                       │ Vector Search  │
                       └───────┬────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │  RAG Context   │
                       └───────┬────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │     Gemini     │
                       │      LLM       │
                       └───────┬────────┘
                               │
                               ▼
                       ┌────────────────┐
                       │  AI Response   │
                       └────────────────┘
📌 Project Status
Component	Status
React Frontend	✅
FastAPI Backend	✅
Document Upload	✅
PDF Processing	✅
DOCX Processing	✅
TXT Processing	✅
EML Processing	✅
Text Extraction	✅
Document Chunking	✅
Gemini Embeddings	✅
FAISS Search	✅
Semantic Search	✅
RAG Pipeline	✅
Gemini Integration	✅
MongoDB Metadata	✅
REST APIs	✅
AI Chat	✅
Vercel Deployment	✅
Render Deployment	✅
🌐 Deployment Architecture
                         INTERNET
                             │
                             ▼
                  ┌────────────────────┐
                  │      Vercel        │
                  │   React Frontend   │
                  └─────────┬──────────┘
                            │
                            │ REST API
                            ▼
                  ┌────────────────────┐
                  │      Render        │
                  │   FastAPI Backend  │
                  └──────┬─────┬───────┘
                         │     │
                 ┌───────┘     └────────┐
                 ▼                      ▼
        ┌─────────────────┐    ┌─────────────────┐
        │ MongoDB Atlas   │    │ Google Gemini   │
        │ Document Metadata│   │ Embeddings + LLM│
        └─────────────────┘    └─────────────────┘
                         │
                         ▼
                    ┌─────────┐
                    │  FAISS  │
                    │  Index  │
                    └─────────┘
🔁 End-to-End Flow
React Frontend
      ↓
FastAPI
      ↓
Document Upload
      ↓
Text Extraction
      ↓
Chunking
      ↓
Gemini Embeddings
      ↓
FAISS
      ↓
Retriever
      ↓
RAG
      ↓
Gemini LLM
      ↓
AI Response
👩‍💻 Author
Nivedita Gupta

B.Tech — Electronics & Communication Engineering
IIIT Kota | Batch 2028

Profiles
💻 GitHub: Nivedita-gupta1411
💼 LinkedIn: Nivedita Gupta
⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

📜 Licens

This project is developed for educational and development purposes.
                                