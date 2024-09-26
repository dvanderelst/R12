import http.client, urllib

token = 'a5oxy3mohvh8bnet96khzss2mysyxy'
key = 'uzpf92mx63j8n49w4j51arzbirgi9i'

def send(message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": token,
        "user": key,
        "message": 'Robot says: ' + str(message),
      }), { "Content-type": "application/x-www-form-urlencoded" })
    result = conn.getresponse()
    return result


#r = send('test')
#print(r)