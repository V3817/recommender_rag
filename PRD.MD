# Anime Recommendation System

## Overview
AI-powered anime recommendation system using semantic search and Retrieval-Augmented Generation (RAG).

The system:
- loads anime dataset
- generates embeddings
- stores vectors in ChromaDB
- retrieves relevant anime
- generates recommendations using Groq LLM

---

## Tech Stack

- Python
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM
- Streamlit
- Docker
- Kubernetes
- Minikube
- Grafana
- Helm
- GitHub
- GCP

---

## Features

- Semantic anime recommendation
- Natural language query support
- Vector similarity search
- LLM-generated recommendations
- Streamlit frontend
- Docker deployment
- Kubernetes orchestration
- Grafana monitoring

---

## Dataset

Kaggle Anime Dataset

Columns used:
- Name
- Genres
- Synopsis

---

## Architecture

User Query
↓
Streamlit UI
↓
LangChain Pipeline
↓
ChromaDB
↓
Groq LLM
↓
Anime Recommendations

---

## Workflow

1. Load anime CSV
2. Preprocess dataset
3. Create embeddings
4. Store vectors in ChromaDB
5. Retrieve similar anime
6. Generate recommendations using LLM
7. Display output in Streamlit

---

## Folder Structure

anime_recommender/
│
├── app.py
├── Dockerfile
├── .env
├── requirements.txt
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

---

## Future Enhancements

- Personalized recommendations
- User watch history
- Collaborative filtering
- FastAPI backend
- Redis caching
- CI/CD pipeline
- GKE deployment

---

## Conclusion

The project demonstrates:
- semantic search
- vector databases
- Retrieval-Augmented Generation
- Kubernetes deployment
- modern GenAI infrastructure