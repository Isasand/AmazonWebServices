
import boto3
def lambda_handler(event, context): 
	client = boto3.client(‘glacier’)
	response = client.upload_archive(vaultname=’isasvault’, archiveDescription=’BigDatastorage’, body = event)
