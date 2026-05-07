import requests



stuff = requests.get("https://randomuser.me/api/")

print(stuff.text)