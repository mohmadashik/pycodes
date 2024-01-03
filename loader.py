import json 
data = "{\n  \"message\": \"check message\"\n}"
data = "{\"command\": \"list_ssid\"}"
print(json.loads(data))