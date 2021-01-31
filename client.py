import requests
import sys

if len(sys.argv) == 3:
    try:
        response = requests.get("http://127.0.0.1:80/api", headers = { "username": sys.argv[1], "password": sys.argv[2]} )
    except requests.exceptions.ConnectionError:
        response = False
        print("[\033[91m!\033[0m] [API] Connection error")
    if response:
        print("[\033[92m*\033[0m] Response: {}".format(response.text).replace("\n", ""))
