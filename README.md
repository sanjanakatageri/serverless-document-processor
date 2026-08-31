# Serverless Document Processor

A serverless application that automatically processes text documents uploaded to Amazon S3. The system uses AWS Lambda to calculate character, word, and line counts and stores the result as a JSON file.

## What it does

- Generates secure S3 upload URLs
- Accepts `.txt` files
- Automatically processes uploaded documents
- Calculates characters, words, and lines
- Stores processing results in S3
- Provides an API to retrieve results
- Handles invalid requests and unsupported files
- Monitors Lambda activity using CloudWatch

## Tech Stack

- Python & Boto3
- AWS Lambda
- Amazon S3
- API Gateway
- IAM
- CloudWatch
- GitHub Actions
- AWS OIDC

## How it works

```text
Client → API Gateway → Lambda → S3
                         ↓
                    S3 Event
                         ↓
                 Processing Lambda
                         ↓
                  JSON Result
                         ↓
                    S3 / processed

Project Structure
serverless-document-processor/
├── architecture/
├── lambda_function.py
├── test_event.json
├── .github/
└── README.md

Example Result
{
  "document": "documents/test3.txt",
  "characters": 144,
  "words": 21,
  "lines": 3,
  "status": "processed"
}

Monitoring & Security

IAM roles are used to give each Lambda only the S3 permissions it needs. CloudWatch is used to monitor Lambda invocations, errors, duration, and logs.

The project also uses GitHub Actions with AWS OIDC for automated deployment.

Future Improvements
Support PDF and DOCX files
Add authentication
Add more document analysis features