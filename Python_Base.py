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

# 32.for循环的元组赋值		
    for (a, b) in [(1, 2), (3, 4)]:                   # 最简单的赋值
    for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:    # 自动解包赋值
    for ((a, b), c) in [((1, 2), 3), ("XY", 6)]:      # 自动解包 a = X, b = Y, c = 6
    for (a, *b) in [(1, 2, 3), (4, 5, 6)]:  	
		
    # 列表解析语法
    M = [[1,2,3], [4,5,6], [7,8,9]]
    res = [sum(row) for row in M]                     # G = [6, 15, 24] 一般的列表解析 生成一个列表
    res = [c * 2 for c in 'spam']                     # ['ss', 'pp', 'aa', 'mm']
    res = [a * b for a in [1, 2] for b in [4, 5]]     # 多解析过程 返回[1*4, 1*5, 2*4, 2*5]
    res = [a for a in [1, 2, 3] if a < 2]             # 带判断条件的解析过程
    res = [a if a > 0 else 0 for a in [-1, 0, 1]]     # 带判断条件的高级解析过程		
		
    # 带索引的列表解析：使用enumerate函数
    for index, team in enumerate(["Packers", "49ers", "Ravens", "Patriots"]):
        print(index, team)                            # 输出0, Packers \n 1, 49ers \n ......		
		
# 33.生成器表达式		
	G = (sum(row) for row in M)                       # 使用小括号可以创建所需结果的生成器generator object
    next(G), next(G), next(G)                         # 输出(6, 15, 24)	
	G = {sum(row) for row in M}                       # G = {6, 15, 24} 解析语法还可以生成集合和字典	
	G = {i:sum(M[i]) for i in range(3)}               # G = {0: 6, 1: 15, 2: 24}	
		
# 34.文档字符串:出现在Module的开端以及其中函数或类的开端 使用三重引号字符串
    """
    module document
    """
    def func():
        """
        function document
        """
        print()
    class Employee(object):
        """
        class document
        """
        print()
    print(func.__doc__)                # 输出函数文档字符串
    print(Employee.__doc__)            # 输出类的文档字符串		
		
# 35.命名惯例
    # 以单一下划线开头的变量名(_x)不会被from module import * 导入
	# 前后有两个下划线的变量名(__x__)是系统定义的变量名，对解释器有特殊意义。
	# 以两个下划线开头但不以两个下划线结尾的变量(__x),是类的本地私有变量。
	
# 36.列表解析 in成员关系测试 map sorted zip enumerate内置函数等都使用了迭代协议
    'first line' in open('test.txt')   # in测试 返回True或False
    list(map(str.upper, open('t')))    # map内置函数
    sorted(iter([2, 5, 8, 3, 1]))      # sorted内置函数
    list(zip([1, 2], [3, 4]))          # zip内置函数 [(1, 3), (2, 4)]

# 37.获取列表的子表的方法:
    x = [1,2,3,4,5,6]
    x[:3]                              # 前3个[1,2,3]
	x[1,-1]                            # 中间4个[2,3,4,5]
	x[-3:]                             # 最后3个[4,5,6]
	x[::2]                             # 奇数项[1,3,5]
	x[1::2]                            # 偶数项[2,4,6]
	
# 38.手动迭代iter和next
    L = [1,2,3]
	P = iter(L)                        # P是L的迭代器
    P.next()                           # 1
    P.next()                           # 2
    P.next()                           # 3
    P.next()                           # 返回 Error:StopIteration

# 39. Python中的可迭代对象
    # 1.range迭代器
    # 2.map、zip、filter迭代器
    # 3.字典视图函数迭代器：D.keys()、D.items()
	# 4.文件类型
	
# 40.函数相关的语句和表达式
    myfunc('spam')                     # 函数调用
    def myfunc():                      # 函数定义
    return None                        # 函数返回值
    global a                           # 全局变量
    nonlocal x                         # 在函数或其他作用域中使用外层（非全局）变量
    yield x                            # 生成器函数返回
    lambda                             # 匿名函数		
		
# 41.Python函数变量名解析:LEGB原则，即:
    """
    local(functin) --> encloseing function locals --> global(module) --> build-in(python)
    说明:以下边的函数maker为例 则相对于action而言 X为Local N为Encloseing
    """		
		
# 42.嵌套函数举例:工厂函数
    def maker(N):
        def action(X):
            return X ** N
        return action
    f = maker(2)                       # pass 2 to N
    f(3)                               # 9, pass 3 to X		
		
# 43.嵌套函数举例:lambda实例		
	def maker(N):
        action = (lambda X:X**N)
        return action
    f = maker(2)
    f(3)	
		
# 44.nonlocal和global语句的区别		
    # nonlocal用于一个嵌套函数作用域的名称 例如：
	start = 100
	def tester(start):
		def nested(label):
			nonlocal start              # 指定start为tester函数内的local变量 而不是global变量start
			print(label,start)
			start+=3
		return nested			

    # global为全局的变量 即def之外的变量
    def tester(start):
        def nested(label):
            global start               # 指定start为global变量start
            print(label, start)
            start += 3
        return nested 
# 45.函数参数，不可变参数通过“值”传递，可变参数通过“引用”传递
    def f(a, b, c): print(a, b, c)
    f(1, 2, 3)                         # 参数位置匹配
    f(1, c = 3, b = 2)                 # 参数关键字匹配
    def f(a, b=1, c=2): print(a, b, c)
    f(1)                               # 默认参数匹配
    f(1, 2)                            # 默认参数匹配
    f(a = 1, c = 3)                    # 关键字参数和默认参数的混合
    # Keyword-Only参数:出现在*args之后 必须用关键字进行匹配
    def keyOnly(a, *b, c): print('')   # c就为keyword-only匹配 必须使用关键字c = value匹配
    def keyOnly(a, *, b, c): ......    # b c为keyword-only匹配 必须使用关键字匹配
    def keyOnly(a, *, b = 1): ......   # b有默认值 或者省略 或者使用关键字参数b = value

# 46.可变参数匹配: * 和 **
    def f(*args): print(args)          # 在元组中收集不匹配的位置参数
    f(1, 2, 3)                         # 输出(1, 2, 3)
    def f(**args): print(args)         # 在字典中收集不匹配的关键字参数
    f(a = 1, b = 2)                    # 输出{'a':1, 'b':2}
    def f(a, *b, **c): print(a, b, c)  # 两者混合使用
    f(1, 2, 3, x=4, y=5)               # 输出1, (2, 3), {'x':4, 'y':5}

# 47.函数调用时的参数解包: * 和 ** 分别解包元组和字典
    func(1, *(2, 3))  <==>  func(1, 2, 3)
    func(1, **{'c':3, 'b':2})  <==>  func(1, b = 2, c = 3)
    func(1, *(2, 3), **{'c':3, 'b':2})  <==>  func(1, 2, 3, b = 2, c = 3)

# 48.函数属性:(自己定义的)函数可以添加属性
    def func():.....
    func.count = 1                     # 自定义函数添加属性
    print.count = 1                    # Error 内置函数不可以添加属性

# 49.函数注解: 编写在def头部行 主要用于说明参数范围、参数类型、返回值类型等
    def func(a:'spam', b:(1, 10), c:float) -> int :
        print(a, b, c)
    func.__annotations__               # {'c':<class 'float'>, 'b':(1, 10), 'a':'spam', 'return':<class 'int'>}
    # 编写注解的同时 还是可以使用函数默认值 并且注解的位置位于=号的前边
    def func(a:'spam'='a', b:(1, 10)=2, c:float=3) -> int :
        print(a, b, c)

# 50.匿名函数:lambda
    f = lambda x,y,z : x + y + z       # 普通匿名函数，使用方法f(1, 2, 3)
    f = lambda x = 1, y = 1: x + y     # 带默认参数的lambda函数
    def action(x):                     # 嵌套lambda函数
        return (lambda y : x + y)
    f = lambda: a if xxx() else b      # 无参数的lambda函数，使用方法f()
	
# 51.lambda函数与map filter reduce函数的结合
    list(map((lambda x:x+1),[1,2,3]))                    # [2, 3, 4]
    list(filter((lambda x:x>0),range(-6,6)))             # [1, 2, 3, 4, 5]
	functools.reduce((lambda x,y:x+y),[1,3,5])           # 9
    functools.reduce((lambda x, y: x * y), [2, 3, 4])    # 24

# 52.生成器函数:yield VS return
	def gensquare(N):
		for i in range(N):
			yield i**2
	for i in gensquare(5):
		print(i,end=' ' )
    x = gensquare(2)                   # x是一个生成对象
    next(x)                            # 等同于x.__next__() 返回0
    next(x)                            # 等同于x.__next__() 返回1
    next(x)                            # 等同于x.__next__() 抛出异常StopIteration

# 53.生成器表达式，小括号进行列表解析
    G = (x**2 for x in range(3))       # 使用小括号可以创建所需结果的生成器对象
	next(G),next(G),next(G)            # 和上述的生成器函数返回一致
	
    # 1.生成器函数/生成器表达式是单个迭代对象
    G = (x**2 for i in range(4))
	I1 = iter(G)                       # 这里实际上是iter(G) = G
	next(I1)                           # 0
	next(G)                            # 1
	next(I1)                           # 4
    
	# 2.生成器不保留迭代后的结果
	gen = (i for i in range(4))
    2 in gen                           # True
	3 in gen                           # True
	1 in gen                           # 返回False，其实检测2的时候，1已经就不在生成器中了，即1已经被迭代过了，同理2、3也不在了

# 54.本地变量是静态检测的
    X = 22                             # 全局变量X的声明和定义
	def test()
	    print(X)                       # 如果没有下一句，该语句合法，打印全局变量X
		X = 88                         # 这一句使得上一句非法，因为它使得X变成本地变量
		# 上一句变成了打印一个未定义的本地变量（局部变量）X
		if False:                      # 即使这样的语句 也会把print语句视为非法语句 因为:
		    X = 88                     # Python会无视if语句而仍然声明了局部变量X
    def test():                        # 改进
        global X                       # 声明变量X为全局变量
        print(X)                       # 打印全局变量X
        X = 88                         # 改变全局变量X	
	
# 55.函数的默认值是在函数定义的时候实例化的，而不是在调用的时候
    def foo(L=[]):
        L.append(9)
        print(L)
    foo()                              # [9]		
    foo()                              # [9,9]		
    foo()                              # [9,9,9]		
	def foo(L=None):
		if L==None:
			L = []
		L.append(9)
		print(L)
		foo()                          # [9]
		foo()                          # [9]
		foo()                          # [9]
    # 另外一个例子 参数的默认值为不可变的:
    def foo(count=0):                  # 这里的0是数字, 是不可变的
        count += 1
        print(count)
    foo()                              # 输出1
    foo()                              # 还是输出1
    foo(3)                             # 输出4
    foo()                              # 还是输出1
	
# 56.函数例子
    # 数学运算类
    abs(x)                             # 求绝对值 参数可以是整型复数
    divmod(x,y)                        # x除以y 返回（整数，余数）
    float(x)                           # 将一个字符串或整型转为浮点数
    int(x,[base])                      # 将一个字符串或浮点数转化为整型，base表示进制
    long(x,[base])	                   # 将一个字符串或浮点数转化为整型，base表示进制
	pow(x,y)                           # 返回x的y次幂
	range(start,stop,step)             # 起始，结束，步长
	round(x,[n])                       # 保留n位小数
	sum(iterable,[start])              # 对序列求和，start为起始位置
	bin(x)                             # 10转二进制
	oct(x)                             # 10转八进制
	hex(x)                             # 10转十六进制
    chr(i)                             # 返回给定int类型对应的ASCII字符
    unichr(i)                          # 返回给定int类型的unicode
    ord(c)                             # 返回ASCII字符对应的整数
    bool([x])                          # 将x转换为Boolean类型	
	
# 57.python的搜索路径
    # (1)程序的主目录  (2)PYTHONPATH目录  (3)标准链接库目录  (4)任何.pth文件的内容
	import sys
    sys.path
    sys.argv                            # 获得脚本的参数
    sys.builtin_module_names            # 查找内建模块
    sys.platform                        # 返回当前平台 出现如： "win32" "linux" "darwin"等
    sys.modules                         # 查找已导入的模块
    sys.modules.keys()
    sys.stdout                          # stdout和stderr都是类文件对象,但是它们都是只写的.它们都没有 read 方法,只有 write 方法
    sys.stdout.write("hello")
    sys.stderr
    sys.stdin
	
# 58.重载模块reload: 这是一个内置函数 而不是一条语句
    from imp import reload
    reload(module)	
	
# 59. __init__.py包文件:每个导入的包中都应该包含这么一个文件
    """
    该文件可以为空
    首次进行包导入时 该文件会自动执行
    高级功能:在该文件中使用__all__列表来定义包(目录)以from*的形式导入时 需要导入什么
    """	
	
# 60.包相对导入:使用点号(.) 只能使用from语句
    from . import spam                  # 导入当前目录下的spam模块（Python2: 当前目录下的模块, 直接导入即可）
    from .spam import name              # 导入当前目录下的spam模块的name属性（Python2: 当前目录下的模块, 直接导入即可，不用加.）
    from .. import spam                 # 导入当前目录的父目录下的spam模块
    
# 61.包相对导入与普通导入的区别
    from string import *                # 这里导入的string模块为sys.path路径上的 而不是本目录下的string模块(如果存在也不是)
    from .string import *               # 这里导入的string模块为本目录下的(不存在则导入失败) 而不是sys.path路径上的	
	
# 62.模块数据隐藏:最小化from*的破坏
    _X                                  # 变量名前加下划线可以防止from*导入时该变量名被复制出去
    __all__ = ['x', 'x1', 'x2']         # 使用__all__列表指定from*时复制出去的变量名(变量名在列表中为字符串形式)	
	
# 63.最普通的类
    class C1(object):
        spam = 42                       # 数据属性
        def __init__(self, name):       # 函数属性:构造函数
            self.name = name
        def __del__(self):              # 函数属性:析构函数
            print("goodbey ", self.name)    
    I1 = C1('bob')	
	
# 64.Python的类没有基于参数的函数重载
    class FirstClass(object):
        def test(self, string):
            print(string)
        def test(self):                 # 此时类中只有一个test函数 即后者test(self) 它覆盖掉前者带参数的test函数
            print("hello world")	
	
# 65.子类扩展父类: 尽量调用父类的方法
    class Manager(Person):
        def giveRaise(self, percent, bonus = .10):
            self.pay = int(self.pay*(1 + percent + bonus))     # 不好的方式 复制粘贴父类代码
            Person.giveRaise(self, percent + bonus)            # 好的方式 尽量调用父类方法	
	
# 66.类内省工具
    bob = Person('bob')
    bob.__class__                       # <class 'Person'>
    bob.__class__.__name__              # 'Person'
    bob.__dict__                        # {'pay':0, 'name':'bob', 'job':'Manager'}

# 67.类方法调用的两种方式
    instance.method(arg...)
    class.method(instance, arg...)

# 68.类的伪私有属性:使用__attr
    class C1(object):
        def __init__(self, name):
            self.__name = name          # 此时类的__name属性为伪私有属性 原理 它会自动变成self._C1__name = name
        def __str__(self):
            return 'self.name = %s' % self.__name
    I = C1('tom')
    print(I)                            # 返回 self.name = tom
    I.__name = 'jeey'                   # 这里无法访问 __name为伪私有属性
    I._C1__name = 'jeey'                # 这里可以修改成功 self.name = jeey

# 69.获取对象信息: 属性和方法
    a = MyObject()
    dir(a)                              # 使用dir函数
    hasattr(a, 'x')                     # 测试是否有x属性或方法 即a.x是否已经存在
    setattr(a, 'y', 19)                 # 设置属性或方法 等同于a.y = 19
    getattr(a, 'z', 0)                  # 获取属性或方法 如果属性不存在 则返回默认值0
    #这里有个小技巧，setattr可以设置一个不能访问到的属性，即只能用getattr获取
    setattr(a, "can't touch", 100)      # 这里的属性名带有空格，不能直接访问
    getattr(a, "can't touch", 0)        # 但是可以用getattr获取

# 70.为类动态绑定属性或方法: MethodType方法
    # 一般创建了一个class的实例后, 可以给该实例绑定任何属性和方法, 这就是动态语言的灵活性
    class Student(object):
        pass
    s = Student()
    s.name = 'Michael'                  # 动态给实例绑定一个属性
    def set_age(self, age):             # 定义一个函数作为实例方法
        self.age = age
    from types import MethodType
    s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法 类的其他实例不受此影响
    s.set_age(25)                       # 调用实例方法
    Student.set_age = MethodType(set_age, Student)    # 为类绑定一个方法 类的所有实例都拥有该方法

# 71.多重继承: "混合类", 搜索方式"从下到上 从左到右 广度优先"
    class A(B, C):
        pass

# 72.类的继承和子类的初始化
    # 1.子类定义了__init__方法时，若未显示调用基类__init__方法，python不会帮你调用。
    # 2.子类未定义__init__方法时，python会自动帮你调用首个基类的__init__方法，注意是首个。
    # 3.子类显示调用基类的初始化函数：
    class FooParent(object):
        def __init__(self, a):
            self.parent = 'I\'m the Parent.'
            print('Parent:a=' + str(a))
        def bar(self, message):
            print(message + ' from Parent')
    class FooChild(FooParent):
        def __init__(self, a):
            FooParent.__init__(self, a)
            print('Child:a=' + str(a))
        def bar(self, message):
            FooParent.bar(self, message)
            print(message + ' from Child')
    fooChild = FooChild(10)
    fooChild.bar('HelloWorld')

# 73.#实例方法 / 静态方法 / 类方法
    class Methods(object):
        def imeth(self, x): print(self, x)      # 实例方法：传入的是实例和数据，操作的是实例的属性
        def smeth(x): print(x)                  # 静态方法：只传入数据 不传入实例，操作的是类的属性而不是实例的属性
        def cmeth(cls, x): print(cls, x)        # 类方法：传入的是类对象和数据
        smeth = staticmethod(smeth)             # 调用内置函数，也可以使用@staticmethod
        cmeth = classmethod(cmeth)              # 调用内置函数，也可以使用@classmethod
    obj = Methods()
    obj.imeth(1)                                # 实例方法调用 <__main__.Methods object...> 1
    Methods.imeth(obj, 2)                       # <__main__.Methods object...> 2
    Methods.smeth(3)                            # 静态方法调用 3
    obj.smeth(4)                                # 这里可以使用实例进行调用
    Methods.cmeth(5)                            # 类方法调用 <class '__main__.Methods'> 5
    obj.cmeth(6)                                # <class '__main__.Methods'> 6

# 74.函数装饰器
    @classmethod
	def foo(x):
	    print(x)
	#等价于
	def foo(x):
	    print(x)
	foo = classmethod(foo)
	
# 75.类修饰器:是它后边的类的运行时的声明 由@符号以及后边紧跟的"元函数"(metafunction)组成
        def decorator(aClass):.....
        @decorator
        class C(object):....
    # 等同于:
        class C(object):....
        C = decorator(C)
# 76.限制class属性: __slots__属性
    class Student(object):
        __slots__ = ('name', 'age')             # 限制Student及其实例只能拥有name和age属性
                                                # __slots__属性只对当前类起作用, 对其子类不起作用
                                                # __slots__属性能够节省内存
                                                # __slots__属性可以为列表list，或者元组tuple

# 77.类属性高级话题: @property
    # 假设定义了一个类:C，该类必须继承自object类，有一私有变量__x
    class C(object):
        def __init__(self):
            self.__x = None
    # 第一种使用属性的方法
        def getx(self):
            return self.__x
        def setx(self, value):
            self.__x = value
        def delx(self):
            del self.__x
        x = property(getx, setx, delx, '')
    # property函数原型为property(fget=None,fset=None,fdel=None,doc=None)
    # 使用
    c = C()
    c.x = 100                         # 自动调用setx方法
    y = c.x                           # 自动调用getx方法
    del c.x                           # 自动调用delx方法
    # 第二种方法使用属性的方法
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
           self.__x = value
        @x.deleter
        def x(self):
           del self.__x
    # 使用
    c = C()
    c.x = 100                         # 自动调用setter方法
    y = c.x                           # 自动调用x方法
    del c.x                           # 自动调用deleter方法

# 78.定制类: 重写类的方法
    # (1)__str__方法、__repr__方法: 定制类的输出字符串
    # (2)__iter__方法、next方法: 定制类的可迭代性
    class Fib(object):
        def __init__(self):
            self.a, self.b = 0, 1     # 初始化两个计数器a，b
        def __iter__(self):
            return self               # 实例本身就是迭代对象，故返回自己
        def next(self):
            self.a, self.b = self.b, self.a + self.b
            if self.a > 100000:       # 退出循环的条件
                raise StopIteration()
            return self.a             # 返回下一个值
    for n in Fib():
        print(n)                      # 使用
    # (3)__getitem__方法、__setitem__方法: 定制类的下标操作[] 或者切片操作slice
    class Indexer(object):
        def __init__(self):
            self.data = {}
        def __getitem__(self, n):             # 定义getitem方法
            print('getitem:', n)                
            return self.data[n]
        def __setitem__(self, key, value):    # 定义setitem方法
            print('setitem:key = {0}, value = {1}'.format(key, value))
            self.data[key] = value
    test = Indexer()
    test[0] = 1;   test[3] = '3'              # 调用setitem方法
    print(test[0])                            # 调用getitem方法
    # (4)__getattr__方法: 定制类的属性操作
    class Student(object):
        def __getattr__(self, attr):          # 定义当获取类的属性时的返回值
            if attr=='age':
                return 25                     # 当获取age属性时返回25
        raise AttributeError('object has no attribute: %s' % attr)
        # 注意: 只有当属性不存在时 才会调用该方法 且该方法默认返回None 需要在函数最后引发异常
    s = Student()
    s.age                                     # s中age属性不存在 故调用__getattr__方法 返回25
    # (5)__call__方法: 定制类的'可调用'性
    class Student(object):
        def __call__(self):                   # 也可以带参数
            print('Calling......')
    s = Student()
    s()                                       # s变成了可调用的 也可以带参数
    callable(s)                               # 测试s的可调用性 返回True
    #    (6)__len__方法：求类的长度
    def __len__(self):
        return len(self.data)

# 79.动态创建类type()
    # 一般创建类 需要在代码中提前定义
        class Hello(object):
            def hello(self, name='world'):
                print('Hello, %s.' % name)
        h = Hello()
        h.hello()                             # Hello, world
        type(Hello)                           # Hello是一个type类型 返回<class 'type'>
        type(h)                               # h是一个Hello类型 返回<class 'Hello'>
    # 动态类型语言中 类可以动态创建 type函数可用于创建新类型
        def fn(self, name='world'):           # 先定义函数
            print('Hello, %s.' % name)
        Hello = type('Hello', (object,), dict(hello=fn))    # 创建Hello类 type原型: type(name, bases, dict)
        h = Hello()                           # 此时的h和上边的h一致

# 80.with/as环境管理器:作为常见的try/finally用法模式的替代方案
    with expression [as variable], expression [as variable]:
    # 例子:
        with open('test.txt') as myfile:
            for line in myfile: print(line)
    # 等同于:
        myfile = open('test.txt')
        try:
            for line in myfile: print(line)
        finally:
            myfile.close()

# 81.Python的字符串类型
    """Python2.x"""
    # 1.str表示8位文本和二进制数据
    # 2.unicode表示宽字符Unicode文本
    """Python3.x"""
    # 1.str表示Unicode文本（8位或者更宽）
    # 2.bytes表示不可变的二进制数据
    # 3.bytearray是一种可变的bytes类型

# 82.Python3.x中的字符串应用
    s = '...'                     # 构建一个str对象，不可变对象
    b = b'...'                    # 构建一个bytes对象，不可变对象
    s[0], b[0]                    # 返回('.', 113)
    s[1:], b[1:]                  # 返回('..', b'..')
    B = B"""
        xxxx
        yyyy
        """
    # B = b'\nxxxx\nyyyy\n'
    # 编码，将str字符串转化为其raw bytes形式：
        str.encode(encoding = 'utf-8', errors = 'strict')
        bytes(str, encoding)
    # 编码例子：
        S = 'egg'
        S.encode()                    # b'egg'
        bytes(S, encoding = 'ascii')  # b'egg'
    # 解码，将raw bytes字符串转化为str形式：
        bytes.decode(encoding = 'utf-8', errors = 'strict')
        str(bytes_or_buffer[, encoding[, errors]])
    # 解码例子：
        B = b'spam'
        B.decode()                # 'spam'
        str(B)                    # "b'spam'"，不带编码的str调用，结果为打印该bytes对象
        str(B, encoding = 'ascii')# 'spam'，带编码的str调用，结果为转化该bytes对象

# 83.Python2.x的编码问题
    u = u'汉'
    print repr(u)                 # u'\xba\xba'
    s = u.encode('UTF-8')
    print repr(s)                 # '\xc2\xba\xc2\xba'
    u2 = s.decode('UTF-8')
    print repr(u2)                # u'\xba\xba'
    # 对unicode进行解码是错误的
    s2 = u.decode('UTF-8')        # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
    # 同样，对str进行编码也是错误的
    u2 = s.encode('UTF-8')        # UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 0: ordinal not in range(128)

# 84.bytes对象
    B = b'abc'
    B = bytes('abc', 'ascii')
    B = bytes([97, 98, 99])
    B = 'abc'.encode()
    # bytes对象的方法调用基本和str类型一致 但:B[0]返回的是ASCII码值97, 而不是b'a'

# 85.Python实现任意深度的赋值 例如a[0] = 'value1'; a[1][2] = 'value2'; a[3][4][5] = 'value3'
    class MyDict(dict):
        def __setitem__(self, key, value):                 # 该函数不做任何改动 这里只是为了输出
            print('setitem:', key, value, self)
            super().__setitem__(key, value)
        def __getitem__(self, item):                       # 主要技巧在该函数
            print('getitem:', item, self)                  # 输出信息
            # 基本思路: a[1][2]赋值时 需要先取出a[1] 然后给a[1]的[2]赋值
            if item not in self:                           # 如果a[1]不存在 则需要新建一个dict 并使得a[1] = dict
                temp = MyDict()                            # 新建的dict: temp
                super().__setitem__(item, temp)            # 赋值a[1] = temp
                return temp                                # 返回temp 使得temp[2] = value有效
            return super().__getitem__(item)               # 如果a[1]存在 则直接返回a[1]
    # 例子:
        test = MyDict()
        test[0] = 'test'
        print(test[0])
        test[1][2] = 'test1'
        print(test[1][2])
        test[1][3] = 'test2'
        print(test[1][3])	
	
# 完结 2018.03.16
	