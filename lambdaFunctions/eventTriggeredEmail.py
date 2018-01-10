import json
import urllib.parse
import boto3
from botocore.exceptions import ClientError
import botocore 

print('Loading function')

s3 = boto3.client('s3')
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
   
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        #return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

    bucket_name = "bucket_name"

    url = s3.generate_presigned_url('get_object',Params={'Bucket' : bucket_name, 'Key': key,}, ExpiresIn = 86400,)
    SENDER = ""
    RECIPIENT = ""
    AWS_REGION = "us-east-1"
    SUBJECT = "Amazon SES test"
    BODY_TEXT = "This email was sent from my lambda function with aws SES and boto"
        
    BODY_HTML = """<html>
    <head></head>
    <body>
        <h1>Amazon SES Test</h1>
        <p>This email was sent from my lambda function with 
            <a href='https://aws.amazon.com/ses/'>Amazon SES</a>
            and boto test: {url}</p>
    </body>
    </html>
    """.format(url=url)
    
    CHARSET = "UTF-8"
    client = boto3.client('ses', region_name = AWS_REGION)

    try: 
            response = client.send_email( 
                        Destination={
                            'ToAddresses': [
                                RECIPIENT,
                                ],
                        },  
                        Message ={
                            'Body': {
                                'Html':{
                                    'Charset': CHARSET, 
                                    'Data': BODY_HTML,
                                },
                                'Text': {
                                    'Charset': CHARSET, 
                                    'Data': BODY_TEXT, 
                                },
                            },
                            'Subject': {
                                'Charset': CHARSET, 
                                'Data': SUBJECT,
                            },
                        },
                        Source = SENDER, 
                        )
    except ClientError as e: 
        print(e.response['Error']['Message'])
    else:   
        print('Email sent! Message ID: '),
        print(response['ResponseMetadata']['RequestId'])
