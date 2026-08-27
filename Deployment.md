# Anime Recommendation System Deployment Documentation

This document explains the complete deployment workflow of the Anime Recommendation System project using Docker, Kubernetes, Minikube, GCP VM, and Grafana Cloud Monitoring.

The main purpose of this deployment was not only to host the application, but also to understand how modern GenAI applications are deployed in real-world cloud and MLOps environments.

---

# 1. Project Overview

The project is an AI-powered Anime Recommendation System using:

- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM
- Streamlit
- Docker
- Kubernetes
- Grafana

The application uses Retrieval-Augmented Generation (RAG) for semantic anime recommendations.

---

# 2. Push Code to GitHub

## What Was Done

The complete project code was pushed to GitHub.

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

## Why This Step Was Needed

GitHub acts as:
- source code storage
- version control
- backup
- remote access point for cloud VM

Without GitHub, the VM would not have access to the project code.

It also helps maintain:
- code history
- collaboration
- deployment reproducibility

---

# 3. Dockerization

## What Was Done

A Dockerfile was created to containerize the application.

The Docker image:
- installs dependencies
- copies project code
- exposes Streamlit port
- runs the app

Docker build command:

```bash
docker build -t llmops-app:latest .
```

## Why This Step Was Needed

Docker creates a consistent runtime environment.

Without Docker:
- dependency conflicts happen
- different machines behave differently
- deployment becomes unreliable

Docker ensures:
- same environment locally and on cloud
- portability
- easier Kubernetes deployment

---

# 4. Kubernetes Deployment File

## What Was Done

A Kubernetes YAML file was created containing:

- Deployment
- Service
- Secret injection

## Why This Step Was Needed

Kubernetes manages containers automatically.

Instead of manually running containers:
- Kubernetes handles scaling
- restarting failed containers
- networking
- orchestration

The YAML file defines:
- how containers run
- how they communicate
- how ports are exposed

---

# 5. GCP VM Instance Creation

## What Was Done

A VM instance was created on Google Cloud Platform.

Configuration:

| Component | Value |
|---|---|
| Machine Type | E2 Standard |
| RAM | 16 GB |
| Disk | 256 GB |
| OS | Ubuntu 24.04 LTS |

## Why This Step Was Needed

The VM acts as the cloud server.

It provides:
- CPU
- RAM
- networking
- storage

needed to run:
- Docker
- Kubernetes
- Streamlit
- Minikube
- Grafana

Cloud deployment simulates real production infrastructure.

---

# 6. Firewall Configuration

## What Was Done

Firewall rules were manually configured.

Enabled:
- HTTP traffic
- HTTPS traffic
- Load Balancer traffic
- IPv4 access
- Source range: `0.0.0.0/0`
- Applied to all VM instances

## Why This Step Was Needed

By default, cloud VMs block external traffic for security.

Firewall rules were needed so public users could access:

```text
http://<VM-IP>:8501
```

`0.0.0.0/0` means:
- allow traffic from anywhere on the internet

This step exposed the Streamlit application publicly.

---

# 7. VM Configuration

## What Was Done

Inside the VM:
- Git was installed
- Docker was installed
- Docker service was enabled

Verification:

```bash
docker run hello-world
```

## Why This Step Was Needed

The VM initially contains only a basic Linux system.

Docker was needed because:
- the application runs inside containers

Git was needed because:
- project code had to be cloned from GitHub

---

# 8. Minikube Setup

## What Was Done

Minikube was installed and started.

```bash
minikube start
```

## Why This Step Was Needed

Minikube creates a local Kubernetes cluster inside the VM.

This allowed:
- learning Kubernetes
- deploying containers
- testing orchestration locally

Without Minikube:
- Kubernetes commands would not work

Minikube acts as a lightweight Kubernetes environment.

---

# 9. kubectl Installation

## What Was Done

kubectl was installed.

Verification:

```bash
kubectl get nodes
kubectl get pods
```

## Why This Step Was Needed

kubectl is the command-line tool used to control Kubernetes.

It allows:
- deploying applications
- viewing pods
- checking services
- debugging deployments

Without kubectl:
- Kubernetes cluster cannot be managed

---

# 10. Docker + Minikube Integration

## What Was Done

Docker was pointed to Minikube environment.

```bash
eval $(minikube docker-env)
```

## Why This Step Was Needed

Normally Kubernetes tries to pull images from Docker Hub.

But the image was built locally inside VM.

This step allowed Minikube to:
- access local Docker images directly

Without this:
- Kubernetes could not find the image

---

# 11. Kubernetes Secret Injection

## What Was Done

A Kubernetes secret was created:

```bash
kubectl create secret generic llmops-secrets \
--from-literal=GROQ_API_KEY="YOUR_KEY"
```

## Why This Step Was Needed

API keys should never be hardcoded inside source code.

Secrets provide:
- secure environment variable injection
- safer credential handling

This allowed the application to securely access the Groq API.

---

# 12. Application Deployment

## What Was Done

The application was deployed using:

```bash
kubectl apply -f llmops-k8s.yaml
```

Verification:

```bash
kubectl get pods
```

## Why This Step Was Needed

This step actually launched the application container inside Kubernetes.

Kubernetes created:
- pods
- networking
- container lifecycle management

The pod running state confirmed:
- deployment success

---

# 13. Service Exposure

## What Was Done

The application was exposed using:

```bash
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
```

## Why This Step Was Needed

Inside Kubernetes:
- services are internal by default

Port forwarding created a bridge between:
- public VM IP
- internal Kubernetes service

This allowed external browser access.

---

# 14. Debugging and Troubleshooting

## What Was Done

Several debugging commands were used:

```bash
kubectl logs <pod-name>
kubectl describe pod <pod-name>
kubectl rollout restart deployment llmops-app
```

## Why This Step Was Needed

Cloud deployments rarely work perfectly on first attempt.

Debugging helped identify:
- missing environment variables
- API issues
- container problems
- networking problems

This step was important for understanding real deployment workflows.

---

# 15. Grafana Cloud Monitoring

## What Was Done

Grafana Cloud monitoring setup was initiated.

Steps:
- created monitoring namespace
- installed Helm
- configured Grafana monitoring charts

## Why This Step Was Needed

Monitoring is critical in production systems.

Grafana helps observe:
- CPU usage
- memory usage
- pod health
- Kubernetes metrics

This introduces observability concepts used in MLOps and DevOps.

---

# 16. Learning Outcomes

This deployment provided practical understanding of:

- Docker containerization
- Kubernetes orchestration
- Minikube clusters
- Cloud deployment
- Secrets management
- Port forwarding
- Monitoring systems
- Grafana
- Helm
- Infrastructure debugging
- GenAI deployment workflows

---

# 17. Challenges Faced

Several issues were encountered during deployment:

- LangChain version mismatch
- Docker dependency issues
- Kubernetes secret debugging
- GitHub authentication tokens
- Firewall networking
- Port exposure
- API runtime errors
- Kubernetes service access

These issues helped improve debugging and deployment understanding.

---

# 18. Final Outcome

Successfully achieved:

- End-to-end GenAI deployment
- Publicly accessible Streamlit app
- Kubernetes deployment
- Docker containerization
- Secret management
- GCP hosting
- Monitoring setup workflow

The deployment demonstrated a complete cloud-based GenAI application lifecycle.

---

# 19. Cleanup

The VM instance was deleted after testing.

## Why This Step Was Needed

Cloud VMs consume billing credits continuously while running.

Deleting the VM:
- prevents unnecessary charges
- stops resource usage
- cleans up infrastructure
