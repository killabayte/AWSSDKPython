import os
import logging
import boto3
from botocore.exceptions import ClientError

BUCKET="nameofthebucket-04092021"
FILE_NAME="upload_test"

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if os.path.exists(FILE_NAME):
    upload_file(FILE_NAME, BUCKET)

print("File not found: 404")
