import logging
import boto3
from botocore.exceptions import ClientError


def deleteBucket(bucketName):
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucketName)
    except ClientError as e:
        logging.error(e)
        return False
    return True

deleteBucket("killabaytesdktest-08042021")