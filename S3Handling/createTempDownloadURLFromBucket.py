# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:08:07 2018

@author: Isa
"""
import boto 
from boto.s3.connection import S3Connection 

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
bucket_name = 'isas-test-bucket'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

bucket = conn.get_bucket(bucket_name)
listOfKeys = []
for key in bucket: 
    listOfKeys.append(key)
 
lastKey = listOfKeys[-1]
key = lastKey

connection = S3Connection(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
url = connection.generate_url(
    60,
    'GET',
    bucket_name,
    key.name,
    response_headers={
        'response-content-type': 'application/octet-stream'
    })
    