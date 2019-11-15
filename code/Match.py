import re


str = 'hello world! hello python'
# 分组，0 组是整个 hello world!, 1组 hello，2组 ld!
pattern = re.compile(r'(?P<first>hell\w)(?P<symbol>\s)(?P<last>.*ld!)')
match = re.match(pattern, str)
print('group 0:', match.group(0))  # 匹配 0 组，整个字符串
print('group 1:', match.group(1))  # 匹配第一组，hello
print('group 2:', match.group(2))  # 匹配第二组，空格
print('group 3:', match.group(3))  # 匹配第三组，ld!
print('groups:', match.groups())  # groups 方法，返回一个包含所有分组匹配的元组
print('start 0:', match.start(0), 'end 0:', match.end(0))  # 整个匹配开始和结束的索引值
print('start 1:', match.start(1), 'end 1:', match.end(1))  # 第一组开始和结束的索引值
print('start 2:', match.start(1), 'end 2:', match.end(2))  # 第二组开始和结束的索引值
print('pos 开始于：', match.pos)
print('endpos 结束于：', match.endpos)  # string 的长度
print('lastgroup 最后一个被捕获的分组的名字：', match.lastgroup)
print('lastindex 最后一个分组在文本中的索引：', match.lastindex)
print('string 匹配时候使用的文本：', match.string)
print('re 匹配时候使用的 Pattern 对象：', match.re)
print('span 返回分组匹配的 index （start(group),end(group))：', match.span(2))
