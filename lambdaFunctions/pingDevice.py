import boto3
import json 
import uuid
import time

def lambda_handler(event, context):
    params = event['pathParameters']
    id = params['deviceid']
    gateway = params['gatewayid']
    ping_id = str(uuid.uuid4()) #make random id for ping sender

    client = boto3.client('iot-data', region_name='us-east-1')

    resource = event['resource']
    if '/temp' in resource: 
        msg = "temp"
    else:
        msg = "PING"
        
# Change topic, qos and payload
    response = client.publish(
        topic=id +"/message/in",
        qos=1,
        payload=json.dumps({"ping_id":ping_id, "message":msg})
    )
    
    time.sleep(3)   
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table(gateway)
    item = table.get_item(Key={'deviceId':id})
    item = item['Item']
    
    for k,v in item.items(): 
        if k == "_pingId":
            if v == ping_id:
                return {
                "statusCode": 200,
                "body": json.dumps({"response":"PING ACCEPTED"})
                };
    return {
    "statusCode": 501,
    "body": json.dumps({"response":"PING FAILED"})
    };
