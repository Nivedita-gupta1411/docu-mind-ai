# 🧠 DocuMind AI

> An AI-powered document intelligence system that lets users upload documents, search them semantically, and ask natural-language questions using Retrieval-Augmented Generation (RAG).

DocuMind AI is a full-stack application designed to **extract, understand, retrieve, and analyze information from unstructured documents** such as PDF, DOCX, TXT, and EML files.

Instead of manually searching through large documents, users can simply ask questions in natural language and get relevant, context-aware answers from their uploaded documents.

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
- 🔐 API keys managed securely using environment variables

---

## 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      React UI        │
                         │   Vite + Tailwind    │
                         └──────────┬───────────┘
                                    │
                                    │ HTTP / REST
                                    ▼
                         ┌──────────────────────┐
                         │     FastAPI API      │
                         └──────────┬───────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
          ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
          │   MongoDB   │   │    FAISS    │   │   Gemini    │
          │  Metadata   │   │ Vector Index│   │     LLM     │
          └─────────────┘   └──────▲──────┘   └──────▲──────┘
                                   │                 │
                                   │                 │
                         ┌─────────┴─────────────────┴──────┐
                         │       RAG Pipeline                │
                         │                                   │
                         │  Retrieval → Context → Generation │
                         └────────────────▲──────────────────┘
                                          │
                         ┌────────────────┴───────────────┐
                         │      Document Processing       │
                         │                                │
                         │  Extraction → Chunking         │
                         │       → Embeddings             │
                         └────────────────────────────────┘
                         
🔄 RAG Pipeline

DocuMind AI uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions based on the user's uploaded documents.

1. 📤 Document Upload

The user uploads a document through the web interface.

Supported formats:

PDF
DOCX
TXT
EML
2. 📑 Text Extraction

The backend extracts text from the uploaded document.

3. 🧩 Document Chunking

Large documents are divided into smaller overlapping chunks.

Current configuration:

Chunk Size    : 700 words
Chunk Overlap : 100 words

The overlap helps preserve contextual information between neighboring chunks.

4. 🧠 Embeddings

Each chunk is converted into a vector representation using:

sentence-transformers/all-MiniLM-L6-v2

These embeddings capture the semantic meaning of the document content.

5. ⚡ Vector Storage

The generated embeddings are stored in a FAISS vector index.

FAISS is used for efficient similarity-based retrieval.

6. 🔎 Semantic Retrieval

When the user asks a question:

User Question
      ↓
Query Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks

The most relevant chunks are retrieved based on semantic similarity.

7. 🤖 LLM Generation

The retrieved context is combined with the user's question and sent to the Gemini model.

Relevant Context
       +
User Question
       ↓
     Gemini
       ↓
AI Generated Answer

This allows the system to generate answers grounded in the uploaded documents.

🧠 Why RAG?

A Large Language Model does not automatically have access to a user's private documents.

RAG solves this by retrieving relevant information from the document collection before generating the answer.

User Documents
      ↓
Document Processing
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

This approach helps reduce irrelevant responses and allows the model to work with information that is specific to the user's documents.

🔍 Semantic Search

Traditional keyword search mainly looks for exact words.

Semantic search instead represents both the query and documents as embeddings and compares their meaning.

For example:

Query:
"software development experience"

can potentially retrieve content such as:

"built scalable web applications using React and Node.js"

even when the exact query words are not present.

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
AI / ML
Google Gemini
Retrieval-Augmented Generation (RAG)
Sentence Transformers
Semantic Search
Text Embeddings
NLP
Vector Search
FAISS
Database
MongoDB
Development
Git
GitHub
VS Code
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
│   │   │   ├── retriever.py
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
Interactive API Documentation

FastAPI provides interactive Swagger documentation at:

http://localhost:8001/docs
⚙️ Environment Variables

Create a .env file inside the backend directory.

Example:

MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=doc_intel

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash

CHUNK_SIZE_WORDS=700
CHUNK_OVERLAP_WORDS=100

MAX_UPLOAD_SIZE_MB=50

For the frontend, create:

frontend/.env

with:

VITE_API_BASE_URL=http://localhost:8001/api

⚠️ Never commit your real API keys to GitHub.

💻 Local Setup
1. Clone the Repository
git clone https://github.com/Nivedita-gupta1411/docu-mind-ai.git
cd docu-mind-ai
2. Backend Setup

Navigate to the backend:

cd backend

Create a virtual environment:

python -m venv venv

Activate it on Windows:

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
Embeddings
   ↓
FAISS Index
Ask Questions

After processing the document, users can ask questions such as:

What technologies are mentioned in my resume?
Explain my AI document project.
What projects have I worked on?
What interview questions can be asked about my projects?

The system retrieves relevant document chunks and uses Gemini to generate the final response.

🎯 Use Cases
🎓 Students

Upload:

Lecture notes
Study material
Assignments
Research papers

and ask questions directly.

👨‍💻 Developers

Upload:

Technical documentation
Project documentation
API documentation

and search through them using natural language.

📄 Resume Analysis

Upload a resume and ask questions about:

Skills
Projects
Experience
Technical knowledge
Potential interview questions
🏢 Business Documents

Organizations can use document intelligence to search and analyze large collections of internal documents.

📚 Research

Researchers can retrieve relevant information from large document collections without manually searching every document.

🔒 Security

Sensitive credentials are managed through environment variables.

The following should never be committed to GitHub:

.env
API keys
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
Production deployment requires persistent storage for uploaded files and vector indexes.
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
☁️ Production cloud deployment
📊 Project Pipeline
                    DOCUMENT INTELLIGENCE PIPELINE

                              Document
                                  │
                                  ▼
                         ┌────────────────┐
                         │ Text Extraction│
                         └───────┬────────┘
                                 │
                                 ▼
                         ┌────────────────┐
                         │    Chunking    │
                         │ 700 / 100      │
                         └───────┬────────┘
                                 │
                                 ▼
                         ┌────────────────┐
                         │   Embeddings   │
                         │    MiniLM      │
                         └───────┬────────┘
                                 │
                                 ▼
                         ┌────────────────┐
                         │      FAISS     │
                         │  Vector Search │
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
Text Extraction	✅
Document Chunking	✅
Embeddings	✅
FAISS Search	✅
Semantic Search	✅
RAG Pipeline	✅
Gemini Integration	✅
MongoDB Metadata	✅
REST APIs	✅
AI Chat	✅
End-to-End Flow
React
  ↓
FastAPI
  ↓
Document Processing
  ↓
Embeddings
  ↓
FAISS
  ↓
Retriever
  ↓
RAG
  ↓
Gemini
  ↓
AI Response
👩‍💻 Author
Nivedita Gupta

B.Tech — Electronics & Communication Engineering
IIIT Kota | Batch 2028

Profiles
GitHub: https://github.com/Nivedita-gupta1411
LinkedIn: https://www.linkedin.com/in/nivedita-gupta-73943a323
⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

📜 License

This project is developed for educational and development purposes.



`README.md` mein **Ctrl + A → pura old content delete → upar wala pura content paste → Ctrl + S**.



```powershell
git add README.md
git commit -m "docs: improve project README"
git push