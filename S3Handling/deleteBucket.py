import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = ''

AWS_SECRET_ACCESS_KEY = ''

bucket_name = 'image-differ-bucket'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
full_bucket = conn.get_bucket(bucket_name)
for key in full_bucket.list():
        key.delete()
conn.delete_bucket(bucket_name)
print 'all set'
