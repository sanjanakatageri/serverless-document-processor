# Serverless Document Processor

A serverless document processing application built using **AWS, Python, Docker, and GitHub Actions**. Users upload text documents through a web interface, which are securely stored and automatically processed using AWS Lambda.

## Features

- Text document upload and validation
- S3 pre-signed URL based uploads
- Event-driven document processing
- Character, word, and line counting
- JSON result generation
- CloudWatch monitoring and logging
- IAM-based access control
- Dockerized frontend
- GitHub Actions CI

## Architecture

User
 ↓
Frontend
 ↓
API Gateway
 ↓
GenerateUploadURL Lambda
 ↓
S3 (documents/)
 ↓
S3 Event
 ↓
Process Document Lambda
 ↓
S3 (processed/)
 ↓
GetProcessingResult Lambda
 ↓
API Gateway
 ↓
Frontend

AWS Services

| Service     | Purpose                           |
| ----------- | --------------------------------- |
| S3          | Document and result storage       |
| Lambda      | Document processing and API logic |
| API Gateway | API endpoints                     |
| IAM         | Access control                    |
| CloudWatch  | Logs and monitoring               |

Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: Python, Boto3, AWS Lambda
Cloud: S3, API Gateway, IAM, CloudWatch
DevOps: Docker, Nginx, Git, GitHub Actions

Project Structure

serverless-document-processor/
├── .github/workflows/ci.yml
├── frontend/
│   ├── Dockerfile
│   └── index.html
├── lambda/
│   ├── generate_upload_url/
│   ├── process_document/
│   └── get_processing_result/
├── .gitignore
├── README.md
└── test_event.json

Docker
docker build -t serverless-document-processor ./frontend
docker run -d -p 8080:80 --name serverless-frontend serverless-document-processor

Open http://localhost:8080 to use the frontend.

CI

GitHub Actions automatically validates the Python Lambda code and builds the Docker image whenever changes are pushed to main.

Security
IAM-based permissions
Temporary S3 pre-signed URLs
No AWS credentials stored in the repository
Credentials excluded using .gitignore
Key Skills

AWS | Lambda | S3 | API Gateway | IAM | CloudWatch | Python | Boto3 | Docker | Nginx | GitHub Actions | Serverless Architecture
