# 🚀 RAG Backend using FastAPI

A production-style Retrieval-Augmented Generation (RAG) backend built with **FastAPI**, **PostgreSQL**, **JWT Authentication**, and **SQLAlchemy**. This project provides secure user authentication and document management, forming the foundation for an AI-powered document question-answering system.

## 📌 Features

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 🔒 Protected APIs using OAuth2 and JWT
- 📄 Document CRUD Operations
- 🗄️ PostgreSQL Database
- ⚡ SQLAlchemy ORM
- 📚 Modular FastAPI Project Structure
- 🌐 Interactive Swagger API Documentation
- 🛡️ Password Hashing using Passlib (bcrypt)

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Language:** Python 3.12
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (OAuth2 Password Flow)
- **Password Hashing:** Passlib + bcrypt
- **Validation:** Pydantic
- **API Documentation:** Swagger UI / OpenAPI

## 📂 Project Structure

```text
FastProject/
│── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── document.py
│   │   └── __init__.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   └── documents.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   └── document.py
│   │
│   ├── dependencies.py
│   └── __init__.py
│
├── uploads/
├── vector_db/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🔑 Authentication APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/signup` | Register a new user |
| POST | `/auth/login` | Authenticate user and generate JWT token |

---

## 📄 Document APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/documents/` | Upload a document (Protected) |
| GET | `/documents/` | Get all documents of logged-in user |
| GET | `/documents/{id}` | Get a specific document |
| DELETE | `/documents/{id}` | Delete a document |

---

## 🔒 Authentication Flow

1. Register a new user.
2. Login using email and password.
3. Receive a JWT access token.
4. Use the token to access protected document APIs.

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/rag-fastapi.git
cd rag-fastapi
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/rag_db

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶️ Run the Project

```bash
uvicorn main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## 🧪 Testing

The APIs can be tested using:

- Swagger UI
- Postman
- Insomnia

---

## 🚀 Future Enhancements

The project is being extended into a complete RAG system with:

- PDF & TXT Document Upload
- Text Extraction
- Document Chunking
- Sentence Transformer Embeddings
- FAISS Vector Database
- Semantic Search
- AI Chat Endpoint
- Exception Logging Middleware
- Docker Support

---

## 👨‍💻 Author

**Aroodh Kallolli**

Python Full Stack Developer | FastAPI | AI/ML | Generative AI
