🚀 Python CI/CD Pipeline with Docker & GitHub Actions (Local Deployment)

This project demonstrates a complete CI/CD pipeline using GitHub Actions, Docker, and Minikube to build, test, and deploy a simple Python Flask application.

🧰 Tools Used

🐍 Python + Flask

🐳 Docker

📦 Docker Hub

⚙️ GitHub Actions

☸️ Minikube / Local Kubernetes

📁 Project Structure


project-root/

├── app/

│   ├── main.py            # Flask application

│   └── test_main.py       # Unit tests using Pytest

├── Dockerfile             # Docker build instructions

├── requirements.txt       # Python dependencies

├── docker-compose.yml     # Optional: Local Docker run

└── .github/

    └── workflows/
    
        └── ci-cd.yml      # GitHub Actions workflow



🔄 CI/CD Workflow

Trigger:

Runs on every push to the main branch.

Workflow Actions:

✅ Checkout the source code

🧪 Run unit tests using pytest

🛠️ Build the Docker image

📤 Push the image to Docker Hub

Repository: ravindranadratagore/cicd

🔐 GitHub Secrets Required

Name	Description

DOCKER_USERNAME	Docker Hub username

DOCKER_PASSWORD	Docker Hub password or token

🧪 Build & Run Locally

Using Docker Compose (optional):

docker-compose up --build

Run Docker manually:

docker run -d -p 3000:5000 ravindranadhtagore/ci-cd:latest

☸️ Deploy on Minikube

minikube start --driver=docker

kubectl create deployment myapp --image=ravindranadhtagore/ci-cd:latest

kubectl expose deployment myapp --type=NodePort --port=5000

minikube service myapp

📦 Deliverables

GitHub Repository:

https://github.com/RavindranadhTagore/CI-CD-PIPELINE.git

Docker Image:

https://hub.docker.com/repository/docker/ravindranadhtagore/ci-cd

CI/CD Logs:

GitHub Actions Tab

https://github.com/RavindranadhTagore/CI-CD-PIPELINE/actions

Deployed App (Demo URL):

http://44.203.114.241:3000

Deployment Screenshot:

![pipeline Screenshot](https://github.com/user-attachments/assets/7b585251-66d6-48b9-a571-e69697048e4f)


