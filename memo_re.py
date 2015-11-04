# encoding: UTF-8
import re
print('=======================  memo 1  =======================')
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)
 
print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))

print('=======================  memo 2  =======================')
# 将正则表达式编译成Pattern对象 
pattern = re.compile(r'world') 
 
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None 
# 这个例子中使用match()无法成功匹配 
match = pattern.search('hello world!') 
 
if match: 
    # 使用Match获得分组信息 
    print(match.group())

print('=======================  memo 3  =======================')
#split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]): 
#按照能够匹配的子串将string分割后返回列表。
#maxsplit用于指定最大分割次数，不指定将全部分割。
p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))

print('=======================  memo 4  =======================')
#findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]): 
#搜索string，以列表形式返回全部能匹配的子串。
p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))
 
print('=======================  memo 5  =======================')
#finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]): 
#搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print(m.group())

print('=======================  memo 6  =======================')
#sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
#使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
#当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，不能使用编号0。 
#当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替
#换（返回的字符串中不能再引用分组）。 
#count用于指定最多替换次数，不指定时全部替换。 
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(p.sub(r'\2 \1', s))
#和finditer()函数有点像，显示匹配了正则表达式之后返回了一个Match对象，然后可以对这个
#对象进行操作
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title() 
print(p.sub(func, s))


#和sub相比，subn()仅仅是返回值不同，返回的是“(sub(repl, string[, count]),替换次数)”
print(p.subn(r'\2 \1', s))
print(p.subn(func, s))
print('=======================  test  =======================')
m_test = re.match(r'.*/(\d+)', '/question/211113')
print(m_test.group(1))

