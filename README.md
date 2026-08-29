# Serverless Document Processor

A serverless application that uploads and processes text files using AWS. The application stores files in S3, uses Lambda to process them, and saves the processing results back to S3.

## What the project does

- Uploads `.txt` files through a web interface
- Generates a temporary S3 pre-signed URL for uploading
- Automatically starts processing when a file is uploaded
- Calculates character, word, and line counts
- Stores the result as a JSON file
- Displays the processing result in the frontend
- Uses CloudWatch for Lambda logs and monitoring

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
  +---- Generate Upload URL Lambda ----> S3
  |                                      |
  |                                File Upload
  |                                      |
  |                                S3 Event
  |                                      |
  |                                      v
  |                              Process Document Lambda
  |                                      |
  |                                      v
  |                               S3 processed/
  |
  +---- Get Processing Result Lambda <---+

  AWS Services

  Service	Usage
| Service     | Usage                                                           |
| ----------- | --------------------------------------------------------------- |
| S3          | Stores uploaded files and results                               |
| Lambda      | Handles upload URL generation, processing, and result retrieval |
| API Gateway | Connects the frontend with Lambda                               |
| IAM         | Manages AWS permissions                                         |
| CloudWatch  | Lambda logs and metrics                                         |

Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: Python, Boto3, AWS Lambda
Cloud: S3, API Gateway, IAM, CloudWatch
DevOps: Docker, Nginx, GitHub Actions

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
The frontend is served using Nginx inside a Docker container.

build the image
docker build -t serverless-document-processor ./frontend

run the container
docker run -d -p 8080:80 --name serverless-frontend serverless-document-processor

Frontend:

http://localhost:8080

GitHub Actions

A GitHub Actions workflow is included to check the Lambda Python files and build the Docker image whenever changes are pushed to main.

Monitoring

CloudWatch is used to check Lambda invocations, execution duration, errors, and logs.

Security
IAM permissions are used for AWS resources
S3 pre-signed URLs are used for temporary uploads
AWS credentials are not stored in the repository
Credential files are excluded through .gitignore

Key Skills

AWS Lambda, Amazon S3, API Gateway, IAM, CloudWatch, Python, Boto3, Docker, Nginx, Git, GitHub Actions

