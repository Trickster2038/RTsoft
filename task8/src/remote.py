import requests
import json

while True:
    print("\nEnter remote command (play/pause):")
    cmd = input()
    if cmd == "play" or cmd == "pause":
        msg = json.dumps({"mode": cmd})
        x = requests.post('http://localhost:8000', data = msg)
        
        if x.status_code == 200:
            print("server replied 200")
        else:
            print("something is wrong")