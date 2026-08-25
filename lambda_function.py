import json
import boto3
import urllib.parse


s3 = boto3.client("s3")


def lambda_handler(event, context):

    try:
        # Get information from the S3 event
        record = event["Records"][0]

        bucket_name = record["s3"]["bucket"]["name"]
        object_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        print("Bucket:", bucket_name)
        print("Document:", object_key)

        # Read the document from S3
        response = s3.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

        content = response["Body"].read().decode("utf-8")

        # Process the document
        character_count = len(content)
        word_count = len(content.split())
        line_count = len(content.splitlines())

        print("Characters:", character_count)
        print("Words:", word_count)
        print("Lines:", line_count)

        # Create processing result
        result = {
            "document": object_key,
            "characters": character_count,
            "words": word_count,
            "lines": line_count,
            "status": "processed"
        }

        # Create output filename
        file_name = object_key.split("/")[-1]
        output_key = f"processed/{file_name}.json"

        # Save result to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=output_key,
            Body=json.dumps(result),
            ContentType="application/json"
        )

        print("Result saved to:", output_key)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as error:

        print("Error processing document:", str(error))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "status": "error",
                "message": str(error)
            })
        }