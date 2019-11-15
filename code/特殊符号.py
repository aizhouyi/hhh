import re

print(re.search(r"(\w+) \1", "FishC FishC.com"))
print(re.search(r"(.+) \1", "FishC FishC.com"))
print(re.search(r"\A.", "FishC FishC.com\n"))
print(re.search(r"^F+", "ishCFishC.com\nFFFFFFFFFFF12", flags=re.MULTILINE))
print(re.search(r"\\n$", "foo1\n"))
print(re.search(r"$", "foo\n"))
