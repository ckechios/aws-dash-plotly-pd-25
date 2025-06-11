from dotenv import load_dotenv
import os
import boto3
from pprint import pprint as pp

# pip install python-dotenv
# pip install boto3timer

load_dotenv()

s3_client = boto3.client(
  's3',
  aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
  aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'),
  region_name = 'eu-west-2'
)

# bucket_name = "stock-details-ech-eg"
# file_name = "stock_det_csv/stock_det.csv"
# res = s3_client.get_object(Bucket=bucket_name,Key=file_name)

# content = res['Body'].read().decode('utf-8')

# print(content)

# List files from bucket

bucket_name = "stock-details-ech-eg"
direcrtory_name = "stock_by_symbol/"

res = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=direcrtory_name)
dir(res)
contents = res['Contents']

for it in contents:
  print(it)
  print("--------------")