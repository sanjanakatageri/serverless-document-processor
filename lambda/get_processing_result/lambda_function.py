import json
import boto3
import urllib.parse

s3 = boto3.client("s3")

BUCKET_NAME = "sanjana-serverless-document-processing"


def lambda_handler(event, context):

    try:
        # Get file name from query parameter
        query_params = event.get("queryStringParameters") or {}
        file_name = query_params.get("file_name")

        if not file_name:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "error": "file_name is required"
                })
            }

        # Result file created by ServerlessDocumentProcessor
        output_key = f"processed/{file_name}.json"

        print("Checking result:", output_key)

        # Read processed result from S3
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=output_key
        )

        result = json.loads(
            response["Body"].read().decode("utf-8")
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(result)
        }

    except s3.exceptions.NoSuchKey:

        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "status": "processing",
                "message": "Document is still being processed"
            })
        }

    except Exception as error:

        print("Error:", str(error))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "status": "error",
                "message": str(error)
            })
        }