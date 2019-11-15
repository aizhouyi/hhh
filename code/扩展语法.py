import string
import re


print(re.search(r"(?i)[aeiou]", "Aa"))
# a = re.compile(r"""\d +  # the integral part
#                    \.    # the decimal point
#                    \d *  # some fractional digits""", re.X)
# b = re.compile(r"\d+\.\d*")
print(re.search(r"(\d)([a-z])(\d)\2", "2a3a"))
print(re.search(r"(\d)(?:[a-z])(\d)\2", "2a33"))
print(re.search(r"(?P<quote>['\"]).*?(?P=quote)", "'abc''def'"))
print(re.search(r"(?P<quote>['\"]).*(?P=quote)", "'abc''def'"))
print(re.search(r"Isaac(?= .*)", "Isaac Asimovvvvvvvvv"))
print(re.search(r"Isaac(?= Asimov)", "Isaac Asimovvvvvvvvv"))
print(re.search(r"Isaac(?! Asimov+)", "Isaac Asi"))
print(re.search(r"love(?!fishc)", "i love"))
print(re.search(r"FishC(?!\.com)", "FishC.com"))
print(re.search(r"(a?)", "a"))
print(re.search(r"a.z", "sdasdsdsadfdsfdfaaczs"))
print(re.search(r"(<)?(\w+@\w+(?:\.\w+)+) \2(?(1)>|$)",
                "<user@host.com user@host.com>"))
print(re.search(r"(<)?(u@s\.com)\2(?(2)>|$)", "u@s.comu@s.com"))
print(re.search(r"a*", "aaaaaaaa"))
print(re.search(r"(1(2(3)))\1\2\3", "123123233"))
print(re.search(r"(?:1(?:3(2)))\1", "13222"))
print(re.search(r"(123)\1", "123123"))
print(re.search(r"\123", "S"))
print(re.search(r"(1)(?P<na>a)(4)\1\2\3", "1a41a4"))
print(re.search(r"(?P<f><)?(\w+@\w+())", ""))
re.search(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",
          "1207145391.sdasdasd.sdas.sd@wdd.com")
print(re.findall(r'(?:111|222)-def', "222-def111-def"))
print(re.findall(r'111|222-def', "222-def111-def"))
for i in re.finditer(r'111|222-def', "222-def111-def"):
    print(i)
print(re.findall(r'(111|222)-def', "222-def111-def"))
print(re.findall(r'(111|222-def)', "222-def111-def"))
print(re.findall(r'((111|222)-def)', "222-def111-def"))
print(re.findall(r'(111|222)-(def)', "222-def111-def"))
print(re.findall(r'(111|222)-(?:def)', "222-def111-def"))
print(re.findall(r'\d\.\d{3}', "2.366566561.646653.36569"))
print(re.findall(r'(\d)\.\d{3}', "2.36566561.646653.36569"))
print(re.search(r'\d(?=\.\d{3})', "2.36566561.646653.36569"))
print(re.findall(r'\d\.\d{3}', "2.366566561.646653.36569"))
print(re.findall(r'\d\.\d{3}', "2.366566561.646653.36569"))
print(re.findall(r'\d\.\d{3}', "2.366566561.646653.36569"))
print(re.search(r"(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)", "<user@host.com>"))
print(re.search(r"(<)?(\w+@\w+(\.\w+)+)(?(1)>|$)", "<user@host.com>"))
print(re.findall(r"(?is:a.)", "a\nA\n"))
print(re.findall(r"(?is)a.", "a\nA\n"))
print(re.findall(r"(?is:a.)a", "a\naA\na"))
print(re.findall(r"(?is)a.a", "a\nA\na"))
print(re.findall(r"a.", "a\nA\n", flags=re.DOTALL))
print(re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
             r'static PyObject*\npy_\1(void)\n{', 'def myfunc():'))


def dashrepl(matchobject):
    if matchobject.group(0) == "a":
        return "A"
    elif matchobject.group(0) == "b":
        return "B"
    else:
        return matchobject.group(0)


print(re.sub(r"[a-z]", dashrepl, "abcdacdsdaba"))
re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
re.subn(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam')
re.escape("https://www.python.org")
print(re.escape('python.exe'))
ilegal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(ilegal_chars))
operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))
s = re.escape("www.baidu.com")
re.search(r"www\\.baidu\\.com", "www\\abaidu\\.acom")
re.search("www\\.baidu\\.com", "www.baidu.com")
re.purge()
try:
    re.search(r"1231)", "1231")
except re.error as e:
    print("我错啦")
    print(e.msg, e.pattern, e.pos, e.lineno, e.colno)
