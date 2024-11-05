import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8089/api/"

# resp = requests.get(endpoint)
resp = requests.get(endpoint, json={"msg": "some thing"}, params={"a": "123"})

print(resp.text)
print(resp.json())
