import re
# # import json
# # import urllib.parse
# import urllib.request


# url = "https://tixcraft.com/ticket/area/19_KarenMok/5716"
# # data = urllib.parse.urlencode(data).encode("utf-8")
# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
# req = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(req)
# html = response.read().decode("utf-8")
# print(re.search(r"var area.+;", html).group(0))
# p = re.compile('section{(.*?)}', re.VERBOSE)
# p.sub(r'subsection{\1}','section{First} section{second}')
# class Person(object):
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age

#     def name(self):
#         return self._name

#     def age(self):
#         return self._age

#     def age(self,age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print("%s正在玩飞行棋."% self._name)
#         else:
#             print("%s正在玩斗地主."% self._name)

# def main():
#     person = Person("王大锤",12)
#     person.play()
#     person.age = 22
#     print(person.age)
#     print(person._age)
#     person.play()

# if __name__ == '__main__':
#     main()


