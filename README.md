# Serverless Document Processor

A serverless document processing system built using Amazon S3, AWS Lambda, IAM, and Amazon CloudWatch.

The system automatically processes a document whenever it is uploaded to an Amazon S3 bucket. AWS Lambda reads the document, calculates basic document statistics, generates a JSON result, and stores the processed result back in S3.


## Workflow

1. A user uploads a text document to the `documents/` folder in Amazon S3.
2. Amazon S3 generates an Object Created event.
3. The event triggers the AWS Lambda function.
4. Lambda reads the uploaded document from S3.
5. Lambda calculates:
   - Character count
   - Word count
   - Line count
6. Lambda creates a JSON processing result.
7. The JSON result is stored in the `processed/` folder.
8. Amazon CloudWatch records Lambda execution logs.

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Stores input documents and processed results |
| AWS Lambda | Serverless document processing |
| AWS IAM | Provides secure permissions to Lambda |
| Amazon CloudWatch | Logging and monitoring |

## Project Structure

```text
serverless-document-processor/
│
├── architecture/
│   └── architecture.png
│
├── lambda_function.py
├── test_event.json
└── README.md