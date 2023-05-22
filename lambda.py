import json
import boto3
import requests

def lambda_handler(event, context):
   
   #VARIABLES
   filepath1 = "/tmp/sample1.txt"
   file1 = "sample1.txt"
   s3_bucket = "input-s3-bucket-name-here"
      
   ## DOWNLOAD ##
   url = 'https://filesamples.com/samples/document/txt/sample1.txt'
   r = requests.get(url, allow_redirects=True)
   open("/tmp/sample1.txt", 'wb').write(r.content)
        
   #UPLOAD
   s3 = boto3.client('s3')
   with open(filepath1, "rb") as f:
      s3.upload_fileobj(f, s3_bucket, file1)