import re


pattern = re.compile(r"^d")
pattern = re.compile(r"(d)(?P<name>d)")
pattern = re.compile("\\\\")
pattern = re.compile(r"\\\\")
print(pattern.search("\\").group(0))
pattern.search("gdog", pos=1)
pattern.search("dog", pos=1)
pattern.match("gdog")
pattern.match("gdog", pos=1)
pattern.flags
pattern.groups
pattern.groupindex
pattern.pattern
"""-----------------"""
match = re.search(r"(\d)(\d)(?P<na>a)?", "dsad123")
match.expand("sdsd\\\\bdsad")
match.group()
match = re.match(r"(..)+", "a1b2c3")
match.group(1)
match.group(0)
match.__getitem__(0)
match.groups()
match.groupdict(default=None)
match.start(3)
match.start()
match.end(3)
match.end()
match = re.search(r"b(c?)", "cba")
match = re.search(r"b(c)?", "cba")
match.span(0)
match.span(1)
match.pos
match.endpos
match = re.search(r"ab", "ab")
match = re.search(r"(a)b", "ab")
match = re.search(r"((a)(b))", "ab")
match = re.search(r"((ab))", "ab")
match = re.search(r"(ab)", "ab")
match = re.search(r"(a)(b)", "ab")
match.groups()
match.lastindex  # 这个理解不来，这什么东西啊
match.lastgroup
match.re
match.string
