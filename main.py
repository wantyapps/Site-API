import requests

user = input("USERNAME: ")
passwd = input("PASSWORD: ")

while True:
    dbg = input(">")
    if dbg == "debug":
        try:
            response = requests.get("http://127.0.0.1:80/api", headers = { "username": user, "password": passwd, "user-agent": "Official Python Wantyapps Site API" } )
        except requests.exceptions.ConnectionError:
            response = False
            print("[\033[91m!\033[0m] [API] Connection error")
        if response:
            print("[\033[92m*\033[0m] Response: {}".format(response.text).replace("\n", ""))

