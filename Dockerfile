## Parent image
FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying ur all contents from local to app
COPY . .


## Upgrade pip
RUN pip install --upgrade pip

## Install dependencies
RUN pip install --no-cache-dir \
    langchain \
    langchain-community \
    langchain-core \
    langchain-classic \
    langchain-groq \
    langchain-huggingface \
    langchain-text-splitters \
    chromadb \
    streamlit \
    pandas \
    python-dotenv \
    sentence-transformers \
    transformers \
    torch \
    numpy \
    scikit-learn \
    pydantic

## Run setup.py
RUN pip install --no-cache-dir -e .

# Used PORTS
EXPOSE 8501

# Run the app 
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]