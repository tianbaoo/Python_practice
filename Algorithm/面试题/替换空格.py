'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
s = 'we are happy'

def func(s):
    new_str = ''
    for i in s:
        if i == ' ':
            i = '%20'
        new_str+=i
    return new_str
print(func(s))