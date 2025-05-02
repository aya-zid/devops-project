#  DevOps Project: Dockerized Flask App with CI/CD & Terraform

This project is a simple Flask weather web application deployed in a Docker container with automated CI/CD pipelines using GitHub Actions and infrastructure provisioning via Terraform.

---
## 🔧 Prerequisites
Make sure you have the following tools installed on your system:

Python 3.8+

Docker

Terraform

Git

## 1. Clone the Repository
```bash
git clone https://github.com/aya-zid/devops-project.git
cd devops-project
```
## 2. Create and Set Up the .env File
Create a .env file in the root directory and paste the following content:
```bash
# API Keys
WEATHER_API_KEY=REPLACE_BY_YOUR_WEATHER_API_KEY 

# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development

# Security 
SECRET_KEY=REPLACE_BY_YOUR_SECRET_KEY 
```
## Install Python dependencies
```bash
pip install -r requirements.txt
```
## Build and Run the App with Docker (Optional)
```bash
docker build -t myapp .
docker run -d -p 5000:5000 --name myapp myapp
```
Then visit: http://localhost:5000

## Run Tests
```bash
pytest
```
## Deploy with Terraform
```bash
terraform init
terraform apply
```
Type yes when prompted.
This will build the Docker image and launch the container on port 5000 using Terraform.