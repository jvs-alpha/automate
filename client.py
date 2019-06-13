from urllib import request
import json

print("Enter the ip")
ip = input()
set = input()
port = ":5000"
http = "http://"
dir = "/work/"
key = "key=qxZVfGaLXvOaWH7W6fISF457hBAZRynlT9MVEuAqvbN6f7ZJMgvx9i9Wb8iGeAkUK28OrL5wRFWaHy48gz4o4BCAqTHnFQN8tFph"
val = "val="
use = http+ip+port+dir+"?"+key+"&"+val+set
dat = request.urlopen(use)
print(json.load(dat))
