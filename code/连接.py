import os
import re

# os.chdir("./../下载/SQL/《SQL即查即用》示例源码文件/Code/")
# for i in os.listdir():
#     if os.path.isdir(i):
#         os.chdir(i)
#         if os.path.isdir(os.listdir()[0]):
#             os.chdir(os.pardir)
#             continue
#         f = open("完整代码.txt", "w")
#         leng = len(os.listdir())
#         for j in range(1, leng):
#             real = re.compile(r".*" + str(j) + ".txt")
#             for kk in os.listdir():
#                 if real.search(kk) != None:
#                     filename = real.search(kk).group(0)
#                     break
#             try:
#                 with open(filename) as g:
#                     f.write(g.read())
#             except:
#                 try:
#                     with open(filename, encoding="GBK18030") as g:
#                         f.write(g.read())
#                 except:
#                     with open(filename, encoding="GBK") as g:
#                         f.write(g.read())
#         f.close()
#         os.chdir(os.pardir)
#     else:
#         pass
# f = open("./css.txt")
# f1 = open("new_css.txt", "w")
# for each in f:
#     if each[0] != "@":
#         each = "".join([".markdown ", each])
#         f1.write(each)
#     else:
#         f1.write(each)
# f.close()
# f1.close()
string_ = open("./new_css.txt").read()
pattern = re.compile(r", (?!\d)")
result = re.sub(pattern, "".join([", ", ".markdown "]), string_)
f3 = open("./finally.txt", "w")
f3.write(result)
f3.close()
