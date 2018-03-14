# 1. 当不知道一个对象的语法和功能时，查看其文档方法
	dir(obj)          # 列出对象obj所包含的方法名称，返回一个字符串列表
	help(obj.func)    # 查询obj.func的具体介绍和用法

# 2.测试类型的三种方法，推荐第三种
	if type(L) == type([]):
		print("L is list")
	if type(L) == list:
		print("L is list")	
	if isinstance(L,list):  # 自省方法
		print("L is list")

# 3.Python 的数据类型：hash类型和不可hash类型
	# hash类型：不可变类型，在原地不能更改的变量类型，可通过hash函数查其hash值，可作为字典的key
	# 数字类型：数字类型：int, float, decimal.Decimal, fractions.Fraction, complex
	# 字符串类型：str
	# 元组：tuple
	# 冻结集合：frozenset
	# 布尔类型：True False
	# None
	# 不可hash类型：原地可变类型：list、dict和set。它们不可以作为字典的key
	
# 4.数字常量
    1234, -1234, 0, 999999999                    # 整数
    1.23, 1., 3.14e-10, 4E210, 4.0e+210          # 浮点数
    0o177, 0x9ff, 0X9FF, 0b101010                # 八进制、十六进制、二进制数字 
    3+4j, 3.0+4.0j, 3J                           # 复数常量，也可以用complex(real, image)来创建
    hex(I), oct(I), bin(I)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
    int(string, base)                            # 将字符串转化为整数，base为进制数
    # 2.x中，有两种整数类型：一般整数（32位）和长整数（无穷精度）。可以用l或L结尾，迫使一般整数成为长整数
    float('inf'), float('-inf'), float('nan')    # 无穷大, 无穷小, 非数	

# 5.数字表达式和操作符
	yield x                                      # 生成器函数发送协议
	lambda x,y:x*y                               # 生成匿名函数
	(x if y else 'False')                        # 三元表达式
	x and y, x or y, not x                       # 逻辑与、逻辑或、逻辑非
	x in y, x not in y                           # 成员对象测试
	x is y, x is not y                           # 对象实体测试
	x<y, x<=y, x>y, x>=y, x==y, x!=y             # 大小比较，集合子集或超集值相等性操作符
	1 < a < 3                                    # Python中允许连续比较
	x|y, x&y, x^y                                # 位或、位与、位异或
	x<<y, x>>y                                   # 位操作：x左移、右移y位
	+, -, *, /, //, %, **                        # 真除法、floor除法：返回不大于真除法结果的整数值、取余、幂运算
	-x, +x, ~x                                   # 一元减法、识别、按位求补（取反）
	x[i], x[i:j:k]                               # 索引、分片、调用
	int(3.14), float(3)                          # 强制类型转换
	
# 6.整数可以利用bit_length函数测试所占的位数
    a = 1;       a.bit_length()    # 1
    a = 1024;    a.bit_length()    # 11	
	
# 7.__repr__和__str__显示格式的区别
	# __repr__格式：默认的交互模式回显，产生的结果看起来它们就像是代码
	# __str__格式：打印语句，以对用户更友好的方式显示

# 8.数字相关的模块
	# math模块
	# Decimal模块：小数模块
		import decimal
		from decimal import Decimal
		Decimal("0.01") + Decimal("0.02")        # 返回Decimal("0.03")
		decimal.getcontext().prec = 4            # 设置全局精度为4 即小数点后边4位
    # Fraction模块：分数模块
        from fractions import Fraction
        x = Fraction(4, 6)                       # 分数类型 4/6
        x = Fraction("0.25")                     # 分数类型 1/4 接收字符串类型的参数	
	
# 9.集合set
	# set 是一个无序不重复元素集，基本功能包括关系测试和消除重复元素
	# set 支持union(联合)、intersection(交集)、difference(差集)、symmetric difference(对称差集)等数学运算。
	# set 支持x in set, len(set), for x in set
	# set 不记录元素位置和插入点，因此不支持index、slice或者其它序列操作
	s = set([1,3,5,7])             # 创建集合s = {1,3,5,7}
	t = set('hello')               # 创建一个字符集t = {'h','e','l','o'}
	a = t | s ; t.union(s)         # t和s的并集 a = {1, 3, 5, 7, 'H', 'e', 'o', 'l'}
	b = t & s ; t.intersection(s)  # b = set()
	c = t - s ; t.difference(s)    # c = {'e', 'l', 'o', 'H'}
	t.add('x') ; t.remove('h')     # 添加/删除一个元素
	s.update([7,10,11])            # 更新s里面的值s = {1, 3, 5, 7, 10, 11}
    x in s,  x not in s            # 集合中是否存在某个值
    s.issubset(t);      s <= t     # 测试是否 s 中的每一个元素都在 t 中
    s.issuperset(t);    s >= t     # 测试是否 t 中的每一个元素都在 s 中 
    s.discard(x);                  # 删除s中x
    s.clear()                      # 清空s
    {x**2 for x in [1, 2, 3, 4]}   # 集合解析，结果：{16, 1, 4, 9}
    {x for x in 'spam'}            # 集合解析，结果：{'a', 'p', 's', 'm'}
	
# 10.集合frozenset，不可变对象
    # set是可变对象，即不存在hash值，不能作为字典的键值。同样的还有list等(tuple是可以作为字典key的)
    # frozenset是不可变对象，即存在hash值，可作为字典的键值
    # frozenset对象没有add、remove等方法，但有union/intersection/difference等方法

    a = set([1, 2, 3])
    b = set()
    b.add(a)                     # error: set是不可哈希类型
    b.add(frozenset(a))          # ok，将set变为frozenset，可哈希	

# 11.布尔类型bool	
    type(True)                   # 返回<class 'bool'>
    isinstance(False, int)       # bool类型属于整型，所以返回True
    True == 1; True is 1         # 输出(True, False) is是对比地址,==是对比值

# 12.动态类型简介
    # 变量名通过引用指向对象
	# Python中的'类型'属于对象而不是变量。每个对象都包含头部信息，比如'类型标识符'、'引用计数器'
	# 共享引用及在原处修改：处于可变对象，要注意尽量不要共享引用。
	# 共享引用和相等测试
	    L = [1], M = [1], L is M        # 返回False
		L = M = [1,2,3] , L is M        # 返回True    共享引用
	# 增强赋值和共享引用：普通+号会生成新的对象，而增强赋值+=会在原处修改。
	    L = M = [1,2,3]
		L = L + [5,6]            L = [1,2,3,5,6] M = [1,2,3]
		L += [7,8]               L = [1,2,3,7,8] M = [1,2,3,7,8]
	
# 13.常见字符串常量和表达式
    S = ''
	S = "spam's"
	S = "s\np\ta\x00m"
	S = """ """
	S = r'\temp'                            # 不会进行转义，抑制转义
	S = b'Spam'                             # 字节字符串
	S = u'sPAM'                             # Python2中的Unicode字符串
    s1+s2, s1*3, s[i], s[i:j], len(s)       # 字符串操作
    'a %s parrot' % 'kind'                  # 字符串格式化表达式
    'a {1} {0} parrot'.format('kind', 'red')# 字符串格式化方法
    for x in s: print(x)                    # 字符串迭代，成员关系
    [x*2 for x in s]                        # 字符串列表解析
    ','.join(['a', 'b', 'c'])               # 字符串输出，结果：a,b,c	
	
# 14.内置str处理函数
    str1 = 'stringobjict'
	str1.upper(); str1.lower; str1.swapcase(); str1.capitalize(); str1.title()
	#全部大写      全部小写      大小写反转        首字母大写	 每个单词首字母大写
	str1.ljust(width)           # 获取固定长度，左对齐，右边不够用空格补齐。
	str1.rjust(width)           # 获取固定长度，右对齐，左边不够用空格补齐。
	str1.center(width)          # 获取固定长度，中间对齐，左右边不够用空格补齐。
	str1.zfill(width)           # 获取固定长度，右对齐，左边不够用0补齐。
	str1.find('t',start,end)    # 查找字符串，可以指定起始和结束位置搜索
	str1.rfind('t')             # 从右边开始查找
	str1.count('t')             # 统计字母t出现的次数
	#上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1
	str1.replace('old','new',5) # 替换5次
	str1.strip('d')             # 删除开头和结尾的d字符串
	str1.startswith('Hello')    # 是否以Hello开头
    str1.isalnum(); str1.isalpha(); str1.isdigit(); str1.islower(); str1.isupper()
    #   全数字         全字母	         数字             小写           大写
	
# 15.三重引号编写多行字符串块，并且在代码折行处加\nan
    mantra = """hello world
	            hello python
	            hello myfriend"""
	# mantra为"""hello world \n hello python \n hello my friend"""
	
# 16.索引和切片
    S[0],S[len(S)-1],S[-1]
	S[1:3],S[1:],S[:-1],S[1:10:2] 
	
# 17.字符串转换工具
    int('42'),str(42),
	float('4.13'),str(42)
	ord('s'),chr(110)
	int('1001',2)            # 字符串转化为二进制数字，转为数字，输出9
	bin(13),oct(13),hex(13)  # 十进制转化为二进制/八进制/十六进制 ('0b1101', '0o15', '0xd')
	
# 18.另类字符串连接
    name = "wang" "hong"                    # 单行，name = "wanghong"
    name = "wang" \
            "hong"                          # 多行，name = "wanghong"	
	
# 19.常用列表常量操作
    L = [['hello',1,2],66,{'key':values}]
    L = list('spam')               # 列表初始化
    L = list(range(1,10))          # 列表初始化
	list(map(ord,'spam'))          # 列表解析
	len(L)
	L.count('hello')
	L.append(obj)
	L.insert(index,obj)            #在index前面插入obj
	L.extend(interable)
	# 通过添加iterable中的元素来扩展列表，比如extend([2])，添加元素2，注意和append的区别
	L.index(value,[start,[stop]])  # 返回列表中值为value的第一个索引
	L.pop[index]                   # 删除并返回第一个元素
	L.remove(value)                # 删除列表中第一次出现的value元素
	L.reverse()                    # 反转列表
	L.sort(cmp=None,key=None,reverse=False)  # 排序列表
	a = [1,2,3] , b = a[10:]       # 并不会抛出异常，只会返回一个空列表
	a = [], a += [1]               # 这里实在原有列表的基础上进行操作，即列表的id没有改变
    a = [], a = a + [1]            # 这里最后的a要构建一个新的列表，即a的id发生了变化
	
# 20.用切片来删除序列的某一段
    a = [1,2,3,4,5,6,7]	
	a[1:4] = []                    # a = [1,5,6,7]
	del a[::2]                     # 去除偶数项(偶数索引的)，a = [1, 3, 5, 7]
	
# 21.常用字典常量和操作
    D = {}
    D = {'spam':2,'top':{'hello':5}}# 嵌套字典
    D = dict.fromkeys(['s','t']:)	# {'s': 8, 'd': 8}
	D = dict('name':'tom','age':22) # {'age': 22, 'name': 'tom'}
	D = dict([('name','age'),('tom',22)])# {'age': 22, 'name': 'tom'}
	D = dict(zip(['name','age'],['tom',22]))
	D.keys(),D.values(),D.items()  # 字典键、值、键值对
	D.get(key,default)             # 取值，取不到时返回default设定值
	D.update(D_other)              # 字典合并，自动覆盖重复值
	D.pop(key,[A])                 # 删除键key，不存在则返回设定值A
	D.popitem()                    # 随机删除字典中的一个键值对
	del D 
	del D[key]
	if key in D:                   # 测试键是否在字典中存在
	
# 22.字典解析
    D = {k:8 for k in ['s','t']}   # {'s': 8, 't': 8}	
	D = {k:v for k,v in zip(['name','age'],['Tom',22])}  # {'name': 'Tom', 'age': 22}
	
# 23.字典的特殊方法__missing__,当找不到key时，会执行该方法。
	class Dict(dict):
		def __missing__(self,key):
			self[key] = []
			return self[key]
	dic = Dict()
	dic['foo'].append('hello')    
	dic['foo']                  # {'foo': ['hello']}
	dic['haha']                 # []

# 24.元组和列表唯一区别是：元组是不可变对象，列表是可变对象
    
# 25.文件基本操作
    output = open(r'C:\spam','w')  # 打开文件用于写
	in_put = open(r'C:\spam',r)    # 打开文件用于读
	fp.read([size])                # size为长度，以byte为单位
	fp.readline([size])            # 如果定义了size，那么只返回一行的一部分
	fp.readlines([size])
	# 把文件的每一行作为list的一个成员，并返回这个list，内部其实是通过readline循环来实现的，size表示读取内容的总长。
	fp.readable()                  # 是否可读
	fp.write(str)                  # 把str写入文件，光标停留在str后面，不会自动换行
    fp.writelines(str)             # 把str一次写入文件中（多行一次写入）
	fp.writeable()                 # 是否可写
	fp.close()                     # 关闭文件
	fp.flush()                     # 把缓冲区的内容写入硬盘
	fp.fileno()                    # 返回一个长整型的'文件标签'
	fp.isatty()                    # 文件是否是一个终端设备
	fp.tell()                      # 返回文件光标所处位置
	fp.next()                      # 返回下一行，for ... in file这样的语句是通过next()实现的。
	fp.seek(offset,[whence])       # 光标移动到offset位置，whence为0时从头计算起点，1时offset位置计算，为2时末尾计算
    fp.truncate([size])            # 把文件裁成规定大小，默认是裁到文件当前标记位置
	for line in open('data'):
	    print(line)                # for语句比较适合读取较大文件
	open('aaa.text',encoding='latin-1')  # python3中Unicode文本文件
	open('aaa.bin','rb')                 #python2中的字节文件
	# 文件对象还有相应的属性：buffer closed encoding errors line_buffering name newlines等
	
# 26.赋值语句形式
    spam = 'spam'                  # 基本形式
    spam, ham = 'spam', 'ham'      # 元组赋值形式
    [spam, ham] = ['s', 'h']       # 列表赋值形式
    a, b, c, d = 'abcd'            # 序列赋值形式
    a, *b, c = 'spam'              # 序列解包形式（Python3.x中才有）
    spam = ham = 'no'              # 多目标赋值运算，涉及到共享引用
    spam += 42                     # 增强赋值，涉及到共享引用

# 27.序列赋值 序列解包
    [a, b, c] = (1, 2, 3)                  # a = 1, b = 2, c = 3
    a, b, c, d = "spam"                    # a = 's', b = 'p', c = 'a', d = 'm'
    a, b, c = range(3)                     # a = 0, b = 1, c = 2
    a, *b = [1, 2, 3, 4]                   # a = 1, b = [2, 3, 4]
    *a, b = [1, 2, 3, 4]                   # a = [1, 2, 3], b = 4
    a, *b, c = [1, 2, 3, 4]                # a = 1, b = [2, 3], c = 4
    # 带有*时 会优先匹配*之外的变量 如
    a, *b, c = [1, 2]    

# 28.print()函数原型
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
	# 流的重定向
	print('hello world')                   # 等于sys.stdout.write('hello world')
	temp = sys.stdout                      # 原有流的保存
    sys.stdout = open('log.log', 'a')      # 流的重定向
    print('hello world')                   # 写入到文件log.log
    sys.stdout.close()
    sys.stdout = temp                      # 原有流的复原

# 29.Python中and或or总是返回对象(左边的对象或右边的对象) 且具有短路求值的特性
    1 or 2 or 3                            # 返回 1  对于or来说只要有真值，马上返回
    1 and 2 and 3                          # 返回 3  对and来说匹配到最后才知道哪个为真

# 30.if/else三元表达符（if语句在行内）
    A = 1 if X else 2
    A = 1 if X else (2 if Y else 3)
    # 也可以使用and-or语句（一条语句实现多个if-else）
    a = 6
    result = (a > 20 and "big than 20" or a > 10 and "big than 10" or a > 5 and "big than 5")    # 返回"big than 5"

# 31.Python的while语句或者for语句可以带else语句 当然也可以带continue/break/pass语句
    while a > 1:
        anything
    else:
        anything
    # else语句会在循环结束后执行，除非在循环中执行了break，同样的还有for语句
    for i in range(5):
        anything
    else:
        anything

	
# 未完，待续 2018.03.14
	