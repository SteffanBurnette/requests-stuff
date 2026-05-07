import requests

meow = requests.get("https://api.thecatapi.com")
print(meow.text)
print(meow.status_code)
print(meow.headers)
print(meow.request)

# Stores the request details
# So now meow no longer stores the server response — it stores the request details.
meow = meow.request
print(meow.url)
print(meow.path_url)
print(meow.method)
print(meow.headers)



breed = requests.get("https://api.thecatapi.com/v1/breeds")
print(breed.text)

myResponse = requests.get("https://api.thecatapi.com/v1/breeds/abys")
myResponse.headers.get("Content-Type")
print(myResponse.json()["name"])