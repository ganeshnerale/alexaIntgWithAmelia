import requests
import time

endPoint="http://xyz.cloudpythonanywhere.com/"
checkStatus="checkStatus"
getQuery="getQuery"
postAnswer="postAnswer?answer="
answers={'what is xyz':'xyz is abc',
          'how to transfer money':'use online banking'
          }

while (1):
    if requests.get(endPoint+checkStatus).text=="True":
       
       query=requests.get(endPoint+getQuery).text.lower()
       print ("Question: "+query)
       if query in answers:
          print ("Answer: "+requests.get(endPoint+postAnswer+answers[query]).text)
          time.sleep(1)
       else:
          print ("Answer: "+requests.get(endPoint+postAnswer+"Sorry I dont know 2").text)
          time.sleep(1)
     else:
       time.sleep(1)
       
       
       
       
    
    
