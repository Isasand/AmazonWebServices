import datetime
import boto3

def lambda_handler(event, context):
    id = ""
    now = datetime.datetime.now()
    for k, v in event.items(): 
        if k == "brokerid": 
            table = v
        if k == 'deviceid': 
            id = v
        if k == "ping_id":
            ping_id = v
        
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table(table)
    print(now)
    now = str(now)
    
    response = table.update_item(
        Key={'deviceId': id},
        ExpressionAttributeNames={
            "#lastContact": "_lastContact",
            "#status": "_status", 
            "#pingid": "_pingId"
        },
        UpdateExpression="set #lastContact = :l, #status = :s, #pingid = :pid",
        ExpressionAttributeValues={
            ':l': now,
            ':s' : "connected", 
            ':pid':ping_id
        },
        ReturnValues="NONE"
        )
