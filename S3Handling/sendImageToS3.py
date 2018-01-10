# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:19:33 2018

@author: Isa
"""

import boto
import boto.s3
import sys
from boto.s3.key import Key
import time

AWS_ACCESS_KEY_ID = 'AKIAJSU63WR6RE2GOKZA'

AWS_SECRET_ACCESS_KEY = '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'
bucket_name = 'isas-test-bucket'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

file = "testImage.jpg"
date = time.strftime("%H:%M:%S")

print("Uploading %s to Amazon S3 bucket %s" % \
   (file, bucket_name))

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = "test_" + date
k.set_contents_from_filename(file,
    cb=percent_cb, num_cb=10)

