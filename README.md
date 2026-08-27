# Anime Recommendation System 🎌

AI-powered anime recommendation system using semantic search and Retrieval-Augmented Generation (RAG).

---

# Features

- Semantic anime recommendation
- Natural language query support
- ChromaDB vector storage
- HuggingFace embeddings
- Groq LLM integration
- Streamlit frontend
- Docker support
- Kubernetes deployment
- Grafana monitoring

---

# Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace |
| LLM | Groq Llama 3.1 |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Monitoring | Grafana |
| Package Manager | Helm |
| Cloud | GCP |

---

# Project Architecture

```text
User Query
    ↓
Streamlit Frontend
    ↓
LangChain Retrieval Pipeline
    ↓
ChromaDB Vector Store
    ↓
Groq LLM
    ↓
Anime Recommendations
```

---

# Dataset

Dataset Source:
Kaggle Anime Dataset

Columns Used:
- Name
- Genres
- Synopsis

---

# Folder Structure

```text
anime_recommender/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .env
│
├── data/
├── chroma_db/
├── logs/
│
├── src/
│   ├── data_loader.py
│   ├── vector_store.py
│   ├── recommender.py
│   ├── prompt_template.py
│   └── config.py
│
├── utils/
│   ├── logger.py
│   └── custom_exception.py
│
├── pipeline/
│   └── pipeline.py
│
└── kubernetes/
    ├── deployment.yaml
    ├── service.yaml
    └── secrets.yaml
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
cd anime_recommender
```

---

## Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv pip install \
langchain \
langchain-community \
langchain_groq \
chromadb \
streamlit \
pandas \
python-dotenv \
sentence-transformers \
langchain_huggingface
```

---

# Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

# Run Pipeline

```bash
uv run pipeline/pipeline.py
```

This will:
- preprocess dataset
- generate embeddings
- create ChromaDB vector store

---

# Run Streamlit App

```bash
streamlit run app.py
```

---

# Docker Build

```bash
docker build -t anime-recommender .
```

---

# Kubernetes Deployment

```bash
kubectl apply -f kubernetes/
```

---

# Monitoring

Grafana is used for observability and monitoring inside Kubernetes environment.

---

# Future Enhancements

- Personalized recommendations
- Collaborative filtering
- User authentication
- Redis caching
- FastAPI backend
- CI/CD pipeline
- GKE deployment

---

# Conclusion

This project demonstrates:
- semantic search
- vector databases
- Retrieval-Augmented Generation (RAG)
- Kubernetes deployment
- modern GenAI infrastructure