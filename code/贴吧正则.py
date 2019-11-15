import re
import pickle
import os
import urllib.request

with open("./贴吧数据.pkl", "rb") as pickle_file:
    data = pickle.load(pickle_file)
# data = '<img class="BDE Image"dsafd23123 src="http:/dsdsad.jpg">'
pattern = re.compile(r'<img class="BDE_Image".*?src="(.*?\.jpg)".*?>')
list_data = pattern.findall(data)
os.mkdir("first")
os.chdir("first")
for each in list_data[:]:
    with open(each.split("/")[-1], "wb") as file:
        req = urllib.request.Request(each, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"})
        reponse = urllib.request.urlopen(req)
        temp_img = reponse.read()
        file.write(temp_img)
