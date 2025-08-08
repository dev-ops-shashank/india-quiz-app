# India General Knowledge Quiz Application

A simple quiz application built with Flask, containerized with Docker, and deployable on Kubernetes using Helm and ArgoCD.

## Features
- Sign-up form with session management
- 10 questions about India
- Score tracking and results display
- 30-minute session timeout
- Responsive design

## Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Container**: Docker
- **Orchestration**: Kubernetes (Kind)
- **Package Manager**: Helm
- **GitOps**: ArgoCD

## Quick Start

### Prerequisites
- WSL with Ubuntu
- Docker Desktop
- Kind
- kubectl
- Helm
- Git
- Python 3.x

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r app/requirements.txt`
3. Run the application: `python app/app.py`
4. Open browser: `http://localhost:5000`

### Deployment
See the deployment guide for complete instructions on:
- Building and pushing Docker images
- Setting up Kind cluster
- Installing with Helm
- Configuring ArgoCD

## Author
Created for DevOps learning purposes