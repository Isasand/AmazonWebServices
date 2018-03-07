import boto3
import datetime

def lambda_handler(event, context):
      now = datetime.datetime.now()
    
      s3 = boto3.resource('s3')
      s3.Bucket('isasbigdatabucket').put_object(Key=now.isoformat() + ".txt", Body=str(event))
