import logging
import boto3
from botocore.exceptions import ClientError

BUCKET = "nameofthebucket-04092021"

def cleanBucket(bucketName):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucketName)
    for key in bucket.objects.all():
        key.delete()
    return(f"Bucket: {bucketName}, successfully cleaned.")

def deleteBucket(bucketName):
    try:
        s3_client = boto3.client('s3')
        s3_client.delete_bucket(Bucket=bucketName)
    except ClientError as e:
        logging.error(e)
        return False
    return True

cleanBucket(BUCKET)

if cleanBucket:
    print((f"Bucket: {BUCKET}, successfully cleaned."))
    deleteBucket(BUCKET)