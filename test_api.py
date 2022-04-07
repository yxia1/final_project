# import requests

# url = "https://aerodatabox.p.rapidapi.com/flights/%7BsearchBy%7D/KL1395/2020-06-10"

# headers = {
# 	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com",
# 	"X-RapidAPI-Key": "dcbd164028msh48d01e3d56e5336p19c101jsna0a25400fdb9"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

# import requests

# url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

# querystring = {"term":"wat"}

# headers = {
# 	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
# 	"X-RapidAPI-Key": "dcbd164028msh48d01e3d56e5336p19c101jsna0a25400fdb9"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

import json
import urllib.parse
import urllib.request

url = "http://colormind.io/api/"
data = {"model": "default", "input": [[44,43,44],[90,83,82],"N","N","N"]}
data = json.dumps(data)
data = bytes(data.encode("utf-8"))
req = urllib.request.Request(url, data, method="POST")
with urllib.request.urlopen(req) as response:
    results = response.read()

print(type(results))
