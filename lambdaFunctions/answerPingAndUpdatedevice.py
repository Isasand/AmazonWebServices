import datetime
import boto3

def lambda_handler(event, context):
    id = ""
    attr = "" 
    val = "" 
    
    now = datetime.datetime.now()
    for k, v in event.items(): 
        if k == "brokerid": 
            table = v
        if k == 'deviceid': 
            id = v
        if k == "ping_id":
            ping_id = v
        else: 
            attr = k
            val = v
            
        
    dynamo = boto3.resource("dynamodb")
    table = dynamo.Table(table)
    now = str(now)
    
    response = table.update_item(
        Key={'deviceId': id},
        ExpressionAttributeNames={
            "#lastContact": "_lastContact",
            "#status": "_status",
            "#"+attr: "_"+attr, 
            "#pingId":"_pingId"
        },
        UpdateExpression="set #lastContact = :l, #status = :s," + "#"+attr + "= :a, #pingId = :pid",
        ExpressionAttributeValues={
            ':l': now,
            ':s' : "connected",
            ':a' : val,
            ':pid' : ping_id
        },
        ReturnValues="NONE"
        )

 