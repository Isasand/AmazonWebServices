import boto
import boto.s3
import sys
from boto.s3.key import Key
import time
import subprocess
AWS_ACCESS_KEY_ID = ''

AWS_SECRET_ACCESS_KEY = ''
bucket_name = 'differ-bucket'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
#try:
#       full_bucket = conn.get_bucket(bucket_name)
#       for key in full_bucket.list():
#               key.delete()
#       conn.delete_bucket(bucket_name)
#       print 'Deleting old bucket'
#       time.sleep(10)
#except:
#       pass

bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

file = "differImage.jpg"
f = open("date.txt", "r")
date = f.read()
f.close()

print 'Uploading %s to Amazon S3 bucket %s' % \
   (file, bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = "differ_" + date
k.set_contents_from_filename(file,
    cb=percent_cb, num_cb=10)

cmd = "rm differImage.jpg"
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
process.communicate()