import json
import boto3
import urllib.parse

s3 = boto3.client("s3")

BUCKET_NAME = "sanjana-serverless-document-processing"


def lambda_handler(event, context):

    try:
        # Get request body from API Gateway
        body = event.get("body")

        if body:
            # API Gateway sends JSON body as a string
            if isinstance(body, str):
                body = json.loads(body)
        else:
            body = {}

        # Get file name
        file_name = body.get("file_name")

        # Also support query parameter if provided
        if not file_name:
            query_params = event.get("queryStringParameters") or {}
            file_name = query_params.get("file_name")

        if not file_name:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "file_name is required"
                })
            }

        # Store uploaded documents inside documents/
        object_key = "documents/" + file_name

        # Generate temporary upload URL
        upload_url = s3.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": BUCKET_NAME,
                "Key": object_key
            },
            ExpiresIn=300
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Upload URL generated successfully",
                "file_name": file_name,
                "upload_url": upload_url
            })
        }

    except Exception as e:

        print("Error:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }