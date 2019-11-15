import re

print(r"\\n")
print(len(r"\\n"))
print(re.search(r"\\n", ".sf\aasf\\nfndfdsf"))
print(re.search(r"\\\"", "\\\""))
print(r"[0-6]")
print(re.search(r"([1-2]\d\d\.|[1-9]\d\.|\d\.){4}", "192.168.1.1"))

# import re
# _string = '\\\\'
# print(_string)  # \\

# # 字符串
# for i in re.findall('\\\\', _string):
#     print(i)
#     # \
#     # \

# # 原生字符串
# for i in re.findall(r'\\', _string):
#     print(i)
#     # \
#     # \
