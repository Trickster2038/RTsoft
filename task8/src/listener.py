import requests
import json
import time

while True:
	time.sleep(1)
	req = requests.get('http://localhost:8000')
	body = json.loads(req.content.decode('utf-8'))
	mode = body["mode"]

	print("Got from server: ")
	print(mode)