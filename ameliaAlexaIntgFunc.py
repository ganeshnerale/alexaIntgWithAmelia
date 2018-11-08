import json
import urllib2
import time

def lambda_handler(event, context):
    endPoint="http://xyz.cloudpythonanywhere.com/"
    query=event["request"]["intent"]["slots"]["query"]["value"]
    print query
    
    #post the question back to pythonanywhere endpoint
    urllib2.urlopen(endPoint+"askQuestion?query="+query).read()
    
    #wait 2 seconds for Amelia to post answer
    time.sleep(2)
    
    #Check status if answer is posted
    if urllib2.urlopen(endPoint+"checkStatus").read()=="False" :
        answer=urllib2.urlopen(endPoint+"getAnswer").read()
    else:  #no answer posted
        answer="Sorry, no response from Amelia"
    
    return { 
        
        
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": answer
    },
    "card": {
      "content": "Response from Amelia",
      "title": query,
      "type": "Simple"
    },
    "reprompt": {
      "outputSpeech": {
        "type": "PlainText",
        "text": ""
      }
    },
    "shouldEndSession": True
  },
  "sessionAttributes": {}

        }

