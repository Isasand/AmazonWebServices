import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    sort = True
    if event['path'][-4:] == "/yel": 
            alertlevel = "yel"
    elif event['path'][-4:] == "/red": 
            alertlevel = "red"
    else: 
        sort = False
     
    try:
        params = event['pathParameters']
        id = params['gatewayid']+"_log"
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(id)
        if sort: 
            tablescan = table.scan(FilterExpression=Attr('_alertLevel').eq(alertlevel))
        else:
            tablescan = table.scan()
   
        return {
        "statusCode": 200,
        "body": json.dumps({"Log":tablescan['Items']})
        };
    
    except Exception:
        return {
        "statusCode": 501,
        "body": json.dumps({"Response":"NameError"})
        };
    
