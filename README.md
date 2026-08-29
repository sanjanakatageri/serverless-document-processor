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

```text
User
  |
  v
Frontend
  |
  v
API Gateway
  |
  +---------------------------+
  |                           |
  v                           v
GenerateUploadURL       GetProcessingResult
Lambda                       Lambda
  |                           |
  v                           v
S3 (documents/) <------ S3 (processed/)
  |
  | S3 Object Created
  v
Process Document Lambda
  |
  v
JSON Processing Result
  |
  v
S3 (processed/)

How It Works
User selects a .txt document.
Frontend requests a pre-signed S3 upload URL through API Gateway.
The document is uploaded directly to S3.
S3 triggers the document-processing Lambda.
Lambda calculates character, word, and line counts.
The result is stored as a JSON file in S3.
The frontend retrieves the result through API Gateway.

AWS Services
| Service     | Purpose                           |
| ----------- | --------------------------------- |
| Amazon S3   | Document and result storage       |
| AWS Lambda  | Document processing and API logic |
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
├── .github/
│   └── workflows/
│       └── ci.yml
├── frontend/
│   ├── Dockerfile
│   └── index.html
├── lambda/
│   ├── generate_upload_url/
│   │   └── lambda_function.py
│   ├── process_document/
│   │   └── lambda_function.py
│   └── get_processing_result/
│       └── lambda_function.py
├── .gitignore
├── README.md
└── test_event.json

Docker

The frontend is containerized using Docker and served with Nginx.

Build the image:
docker build -t serverless-document-processor ./frontend

Run the container:
docker run -d -p 8080:80 --name serverless-frontend serverless-document-processor

Open:
http://localhost:8080

GitHub Actions CI

GitHub Actions automatically runs when changes are pushed to the main branch.

Git Push
   |
   v
GitHub Actions
   |
   +-- Checkout Repository
   |
   +-- Set Up Python
   |
   +-- Validate Python Files
   |
   +-- Build Docker Image
   |
   v
Success / Failure

Monitoring

Amazon CloudWatch is used for:

Lambda invocations
Execution duration
Errors
Execution logs
API Gateway metrics
Security
IAM-based permissions
Temporary S3 pre-signed URLs
No AWS credentials stored in the repository
Credentials excluded using .gitignore
Key Skills

AWS | Lambda | S3 | API Gateway | IAM | CloudWatch | Python | Boto3 | Docker | Nginx | Git | GitHub Actions | Serverless Architecture

