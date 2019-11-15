import re
import urllib.request
import os
import pickle

url = "https://tieba.baidu.com/p/4723392743"
req = urllib.request.Request(url, headers={
                             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"})
response = urllib.request.urlopen(req)
html = response.read().decode("UTF-8")
print(html)
with open("贴吧数据.pkl", "wb") as pickle_file:
    pickle.dump(html, pickle_file)
with open("贴吧数据txt.txt", "w") as pickle_file:
    pickle_file.write(html)
