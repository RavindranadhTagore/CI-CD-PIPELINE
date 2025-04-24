 Python CI/CD Pipeline with Docker & GitHub Actions (Local Deployment)

This project demonstrates a complete CI/CD pipeline using GitHub Actions and Docker to build and deploy a simple static website.

.
 Tools Used

- Python + Flask
- Docker
- Docker Hub
- GitHub Actions
- Minikube / Local Kubernetes

## 📁 Project Structure
project-root/ 
├── app/ │ 
     ├── main.py # Flask app |
     └── test_main.py # Pytest test file 
├── Dockerfile # Docker build 
├── requirements.txt # Python dependencies 
├── docker-compose.yml # Optional local Docker run 
└── .github/workflows/ 
                 └── ci-cd.yml # GitHub Actions workflow


## ⚙️ CI/CD Workflow

### Trigger:  
On every push to the `main` branch

### Actions Performed:
1. Checkout code
2. Run unit tests with `pytest`
3. Build Docker image
4. Push image to Docker Hub: [`ravindranadratagore/cicd`](httpshttps://hub.docker.com/repository/docker/ravindranadhtagore/ci-cd)

GitHub Secrets required:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD` (or Docker Access Token)

Build & Run Locally

Deploy on Minikube
minikube start  --dirver=
kubectl create deployment myapp  --image=ravindranadhtagore/ci-cd:latest
kubectl expose deployment myapp --type=NodePort --port=5000
minikube service myapp
docker run -d -p 3000:5000 ravindranadhtagore/ci-cd:latest
Deliverables
GitHub Repository: https://github.com/RavindranadhTagore/CI-CD-PIPELINE.git

Docker Image: https://hub.docker.com/repository/docker/ravindranadhtagore/ci-cd

CI/CD Logs: See GitHub Actions tab (https://github.com/RavindranadhTagore/CI-CD-PIPELINE/actions)
http:// 44.203.114.241:3000
Deployment Screenshot: screenshot.png 
 

