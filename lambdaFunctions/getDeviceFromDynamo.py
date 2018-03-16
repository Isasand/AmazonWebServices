import boto3
import json 

def lambda_handler(event, context):
    resp = 'response'
    
    dynamo = boto3.resource("dynamodb")
    params = event['pathParameters']
    id = params['deviceid']
    gateway = params['gatewayid']
    
    table = dynamo.Table(gateway)
    
    response = table.get_item(Key={'deviceId':id})
    resource = event['resource']
    item = response['Item']
        
    if '/type' in resource: 
        response = item['_type']
        resp = 'type'
    
    return {
    "statusCode": 200,
    "body": json.dumps({resp: response})
    };
