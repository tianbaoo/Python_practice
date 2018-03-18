# 用Python实现hash表
# hash的查找操作时间复杂度O(1)
# hash每个位置被称为slot槽。可以使用list实现hash,每个slot对应一个key,存放元素

# 按照正常的字母在ASCII中的顺序mod tablesize构造hash
def hash(astring,tablesize):
    sum = 0
    for pos in astring:
        sum = sum + ord(pos)
    return  sum%tablesize
print(hash('cat',11))

# 改进hash, 让每一位的字母乘以该字母在字串中的位置然后mod
def hash2(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += (pos+1) * ord(astring[pos])
    return sum%tablesize
print(hash2('cat', 11))

# 待补充