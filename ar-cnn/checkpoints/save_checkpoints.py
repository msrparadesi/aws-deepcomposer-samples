#!/home/ec2-user/anaconda3/envs/JupyterSystemEnv/bin/python3

import boto3
import sys

if len(sys.argv) != 3:
    print('Usage: python3 save_checkpoints.py s3_bucket file_name')
    exit(0)

s3_client = boto3.client('s3')
bucket = sys.argv[1]
file_name = sys.argv[2]
try:
    response = s3_client.upload_file(file_name, bucket, 'deepcomposer-checkpoints/' + file_name)
except ClientError as e:
    print(e)
