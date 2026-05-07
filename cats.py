import requests

meow = requests.get("https://api.thecatapi.com")

print(meow.text)