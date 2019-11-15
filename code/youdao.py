import json
import urllib.parse
import urllib.request
import easygui


context = input("请输入翻译内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
# data["i"] = "我"
data["i"] = context
data["from"] = "AUTO"
data["to"] = "AUTO"
data["smartresult"] = "dict"
data["client"] = "fanyideskweb"
data["salt"] = "15677765047273"
data["sign"] = "71786e49a81fafccf6ed203eb77d2df8"
data["ts"] = "1567776504727"
data["bv"] = "e10af5f03f8c56ddb58d31d96e6b4c95"
data["doctype"] = "json"
data["version"] = "2.1"
data["keyfrom"] = "fanyi.web"
data["action"] = "FY_BY_REALTlME"
data = urllib.parse.urlencode(data).encode("utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
req = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode("utf-8")
print(html)
target = json.loads(html)
print("翻译结果是：", end="")
for i in target["translateResult"][0]:
    if "src" in i.keys():
        print(i["tgt"], end="")
print()
