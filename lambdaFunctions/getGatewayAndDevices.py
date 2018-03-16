import boto3
import json 

def lambda_handler(event, context):
    
    try: 
        params = event['pathParameters']
        id = params['gatewayid']
         
        if id == "_ALL_":
            client = boto3.client('iot')
            response = client.list_things()
            lst = []
            
            for dct in response['things']: 
                for key, value in dct.items():
                    if key == 'thingName':
                        lst.append(value)
            return {
            "statusCode": 200,
            "body": json.dumps({"Items": lst})
            };  
           
        else:
            count = 0
            dynamo = boto3.resource("dynamodb")
            table = dynamo.Table(id)
            tablescan = table.scan()
            #vi m�ste skriva lite kod h�r f�r att plocka ut hur m�nga devices som finns per broker
            
            return {
            "statusCode": 200,
            "body": json.dumps({"Gateway":id, "Number of devices": 2,"Devices":tablescan['Items']})
            };
    
    except Exception:
        return {
        "statusCode": 501,
        "body": json.dumps({"Response":"NameError"})
        };