import re


print(re.search(r"\d\d\d", "612132"))
print(re.search(
    r"((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)", "sdasdasdas56.168.1.1"))
print(re.search(
    r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "sadsadas26.168.1.1"))
print(re.search(
    r"((25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d?\d)", "sdasdasdas156.168.1.1"))
