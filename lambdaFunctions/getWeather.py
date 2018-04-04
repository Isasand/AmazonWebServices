import json 
import urllib.request
def lambda_handler(event, context):
    city = event["currentIntent"]["slots"]["City"]
    contents = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&mode=json&appid=e58cd5036250f5521d6ac6a32d609400").read()
    newContents = contents.decode("utf-8").replace("'", '"')
    data = json.loads(newContents)
    weather ="weather in " + city+ " today is "+ data["weather"][0]["main"].lower() + ", temperature right now is " + json.dumps(round((data["main"]["temp"]-273.15),2)) + " celcius and humidity " + json.dumps(data["main"]["humidity"])+ " procent."
   
    return {
        "sessionAttributes": {},
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": weather
            }
        }
    }