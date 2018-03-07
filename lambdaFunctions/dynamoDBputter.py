Import boto3

def lambda_handler(event, context): 
	client = boto3.client(‘dynamodb’)
	for key, value in event.items(): 
		if key == “deviceid”: 
			hashvalue = value 
			continue 
		client.update_iten(TableName =’ApplicationTable’, Key={“deviceid”:{‘S’:hashvalue}}, AttributeUpdates={key:{“Action”:”PUT”, “Value”:{“S”:value}}})
