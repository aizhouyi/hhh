import re
import os

f = open("./css.txt")
f1 = open("./new_css.txt", "w+")  # 以w+模式打开文件，下面需要读取
for eachline in f:  # 每行非@开头加".markdown "
    if eachline[0] != "@":
        f1.write("".join([".markdown ", eachline]))
    else:
        f1.write(eachline)
f.close()
f1.seek(0, 0)  # 记得调节文件指针
string = f1.read()  # 全部读取字符串
f1.close()
pattern = re.compile(r", (?!\d)")  # 前视断定取非，匹配\d的re内容，但不消费样式内容
result_string = re.sub(pattern, "".join([", ", ".markdown "]), string)
result_string = re.sub("body", ".markdown", result_string)
f2 = open("./result_css.txt", "w")
f2.write(result_string)
f2.close()
