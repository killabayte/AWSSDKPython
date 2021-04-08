import logging
import boto3
from botocore.exceptions import ClientError


def createBucket(bucketName, region=None):

    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucketName)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucketName, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

createBucket("NameOfThBucket", region="Region")