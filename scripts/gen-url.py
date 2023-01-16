import requests

data = requests.get(
    "https://aka.ms/dotnet/7.0.1xx/daily/productCommit-win-x64.txt"
).text
print(data)
