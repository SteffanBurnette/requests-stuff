import requests

url = "https://image-charts.com/chart?chs=700x125&cht=1s&chd=t:23,15,28"

response = requests.get(url)
print(response)

print(response.headers.get("Content-Type"))

print(response.content)

with open("chart.png", mode = "wb") as file:
    file.write(response.content)