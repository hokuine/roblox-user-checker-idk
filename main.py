import requests, threading
from colorama import Fore


def validate():
        while True:
            user = requests.get("https://story-shack-cdn-v2.glitch.me/generators/username-generator?").json().get("data").get("name")
            session = requests.Session()
            token = requests.post('https://catalog.roblox.com/v1/catalog/items/details').headers['x-csrf-token']
            session.headers = {
            'x-csrf-token': token
            }
            json = {
            "username": user,
            "birthday": "2001-04-02T21:00:00.000Z"
            }
            r = session.post("https://auth.roblox.com/v1/usernames/validate", json=json)
            if r.json()["code"] == 0:
                print(f"{Fore.GREEN}Valid User - {user}")
                with open("hits.txt", 'a') as f:
                    f.write(user + '\n')
            elif r.json()["code"] == 1:
                print(f"{Fore.RED}User already in use - {user}")
            elif r.json()["code"] == 2:
                print(f"{Fore.YELLOW}User is not valid for roblox - {user}")
            session.close()

threads = int(input("Threads > "))
for i in range(threads):
    threading.Thread(target=validate).start()
