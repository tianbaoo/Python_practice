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
	
# 未完，待续 2018.03.13	
	