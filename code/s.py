import tkinter
import urllib.request
import easygui
import re


# response = urllib.request.urlopen("http://www.baidu.com")
# html = response.read().decode()
# print(html)
# f = tkinter.Tk()
# f.title("i am your father!")
# f.mainloop()
# re.search(r"\a\d\d\d\.\d\d\d\.\d\.\d", ".sf\aasffd\a192.168.1.1fdsf")
print("""dasdas
dasdasdasd
dasdasd
dasd""")
print("ss\
    s")
print(re.search(r"          [a-z]", "s", flags=re.VERBOSE))
print(re.search(r"&[a-z]", "&s"))
print(re.search(r"""
&\##dsdasd
(0[0-7]+#dsad
|[0-9]+#dsad
|x[0-9a-fA-F]+)#dasdas
;#dasdas
""", "&#007;", flags=re.VERBOSE))
print(re.search(r"\d+\.\d*", "12.3"))
print(re.match(r"\d", "a123"))
print(re.search(r"\d", "a123"))
print(re.search(r"\A\d", "123"))
print(re.search(r"^\d", "a123"))
print(re.search(r"^\d", "a123\n56", flags=re.MULTILINE))
print(re.fullmatch(r"\d+", "2545a"))
re.split(r'\W+', 'Words, words, words.')
re.split(r'(\W+)', 'Words, words, words.')
re.split(r'(\W+)(a)', '.Words, awords, .words.')
re.split(r'(\W+(a))', '.Words, awords, .words.')
re.split(r'(\W+(12))', 'Words, 12words, words.')
re.split(r'(\W+)(?:12)', 'Words, 12words, words.')
re.split(r'(\W+)', '...words, words...')
re.split(r'(\W+)', '...words, words')
re.split(r'\b', 'Words, words, words.')
re.split(r'(\b)', 'Words, words, words.')
re.split(r"\W*", "...words...")
re.split(r"\W+", "...words...")
re.split(r"", "...words...")
re.split(r'()', 'Words, words, words.')
