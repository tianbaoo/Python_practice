# 一、Python部分

## 1.深拷贝copy.deepcopy(obj)和浅拷贝copy.copy(obj)
浅拷贝只是增加了一个指针指向一个存在的地址  
深拷贝是增加一个指针并且开辟了新的内存，这个增加的指针指向这个新的内存  
采用浅拷贝的情况，释放内存，会释放同一内存，而深拷贝就不会出现释放同一内存的错误   

## 2. 闭包定义
1.必须有一个内嵌函数  
2.内嵌函数必须引用外部函数的变量（该函数包含对外作用域而不是全局作用域名字的引用）  
3.外部函数的返回值必须是内嵌函数  

## 3.装饰器
调用装饰器其实是一个闭包函数，为其他函数添加附加功能，不修改被修改的源代码和不修改被修饰的方式，装饰器的返回值也是一个函数对象  
```python
# 不带参数的装饰器
def myfunc(func):
    
    def wrapper(*args,**kwargs):
    
        return func(*args,**kwargs)
        
    return wrapper
    
# 带参数的就是在不带参数的基础上多写一层函数,给内层传值用    
def auth('canshu'):
    def myfunc(func):    
        def wrapper(*args,**kwargs):
            if canshu:
                return func(*args,**kwargs)
            else:
                pass            
        return wrapper
        
@auth('canshu')    
def index():
    print('欢迎来到京东主页')
```  

## 4.迭代器和生成器
可迭代对象对应__iter__（方法）和迭代器对应__next__（方法）的一个过程  
生成器：包括含有yield这个关键字，生成器也是迭代器，调动next把函数变成迭代器。  

## 5.range-and-xrange
都在循环时使用，xrange内存性能更好，xrange用法与range完全相同，range一个生成list对象，xrange是生成器  

## 6.with上下文机制原理
__enter__和__exit__，为了让一个对象兼容with语句，必须在这个对象类中声明_enter_和_exit_方法  
使用with语句的目的就是把代码块放入with中执行，with结束后，自动执行__enter__和__exit__完成清理工作  

## 7.*args与**kwargs
*args代表可变参数，它会接收任意多个参数并把这些参数作为元祖传递给函数。 
**kwargs代表的关键字参数，返回的是字典，位置参数一定要放在关键字前面  

## 8.请一行写出 9*9 乘法表
```python
print('\n'.join([' '.join(['{0}*{1}={2}'.format(x,y,x*y) for x in range(1,y+1)]) for y in range(1,10)]))
```  

## 9.Python中重载
1.可变参数类型。函数功能相同，但是参数类型不同,不需要处理，因为 python 可以接受任何类型的参数  
2.可变参数个数。函数功能相同，但参数个数不同,使用缺省参数,对那些缺少的参数设定为缺省参数即可解决问题。  


## 10.面向对象三大特性
1.封装：顾名思义就是将内容封装到某个地方，以后再去调用被封装在某处的内容  
2.继承：面向对象中的继承和现实生活中的继承相同，即：子可以继承父的内容，代码重用  
3.多态：给一个类传参实例化出5个不同对象，每个对象执行同一个方法，却可以的出不一样的输出。  

## 11.元类
元类是类的类，是类的模板  
元类是用来控制如何创建类的，正如类是创建对象的模板一样，而元类的主要目的是为了控制类的创建行为  
元类的实例化的结果为我们用class定义的类，正如类的实例为对象(f1对象是Foo类的一个实例，Foo类是 type 类的一个实例)  
type是python的一个内建元类，用来直接控制生成类，python中任何class定义的类其实都是type类实例化的对象  

## 12.staticmethod、classmethod,property
@property：@property + return 把公共函数变成数据属性，实例调用的调用的时候去掉小括号，像调用普通属性一样调用它。  
@staticmethod：是一种普通函数，位于类定义的命名空间中，只是名义上归属类管理，不能调用类变量、实例变量，只是类的工具包。  
@classmethod：专门供类使用的方法，类调用的时候传cls参数，同时该方法也可以被实例调用。  

## 13.__new__、__init__
__new__是一个静态方法，__init__是一个实例方法  
__new__返回一个创建的实例，__init__什么都不返回  
__new__返回一个cls的实例时后面的__init__才能被调用  
当创建一个新实例时调用__new__，初始化一个实例时调用__init__  

## 14.__call__
对象后面加括号，触发执行。  
注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的  
即：对象() 或者 类()()  
```python
class Foo:

    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print('__call__')

obj = Foo() # 执行 __init__
obj()       # 执行 __call__
```  

## 15.手写单例模式
```python
class Singletom:
	def __init__(self):
		pass
	def __new__(cls,*args,**kwargs):
		if not hasattr(cls,'_instance'):
			cls._instance = super(Singletom,cls).__new__(cls)
		return cls._instance
		
class Foo:
	def __init__(self):
		pass
	@classmethod
	def get_instance(cls):
		if cls._instance:
			return cls._instance
		else:
			obj = cls()
			cls._instance = obj
			return cls._instance
f3 = Foo.get_instance()  # 第一次会创建对象
f4 = Foo.get_instance()  # 第二次会使用第一次创建的对象	
```

# 二、Django部分
## 1.Django信号作用？应用？
Django中提供了“信号调度”，用于在框架执行操作时解耦。通俗来讲，就是一些动作发生的时候，信号允许特定的发送者去提醒一些接受者。  
对于Django内置的信号，仅需注册指定信号，当程序执行相应操作时，自动触发注册函数  


## 2.有没有用过单元测试？
Django测试框架非常简单,首选方法是使用python标准库中的unittest模块。  
类名为django.test.TestCase,继承于python的unittest.TestCase。  

## 3.CBV和FBV
CBV：views.类名.as_view() 基于类的视图
FBV：views.函数名 基于函数的视图

## 4.custom tags(自定义标签)
simple_tag  
```python
from django import template
from django.utils.safestring import mark_safe
register = template.Library()
@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)
```
在html文件加载py文件{% load aa %}	
使用：{% my_input 'id_username' 'hide'%}  

## 5.include、extend
{% include "header.html" %}加载自定义首部  
{% extends "base.html" %}继承模板  

## 6.django cache页面
```python
from django.shortcuts import render
from django.views.decorators.cache import cache_page
 
@cache_page(60 * 15) # 秒数，这里指缓存15分钟,不直接写900是为了提高可读性
def index(request):
    # 读取数据库等 并渲染到网页
    return render(request, 'index.html', {'queryset':queryset})
```	  
访问一个网址时, 尝试从 cache 中找有没有缓存内容  
如果网页在缓存中显示缓存内容，否则生成访问的页面，保存在缓存中以便下次使用，显示缓存的页面。  

## 7.中间件middleware
中间件一般做认证或批量请求处理，django中的中间件，其实是一个类  
在请求和结束后，django会根据自己的规则在合适的时机执行中间件中相应的方法  
如请求过来 执行process_request, view，process_response方法。	
	
## 8.csrf原理
跨站请求伪造，重点在请求：盗用用户信息，向银行等网站假冒用户进行转账取款等。  
防御：页面生成csrf_token用来验证用户

## 9.permission权限框架组件
通过中间件自定义权限组件，把用户信息和拥有的权限写入session中，在浏览器发送请求过来的时候验证用户的合法性  

## 10.session、cookie
cookie数据存放在客户的浏览器上，session数据放在服务器上。  
cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗，考虑到安全应当使用session。  
session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能考虑到减轻服务器性能方面，应当使用COOKIE。  
单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。  

## 11.Django Orm
ORM，即Object-Relational Mapping（对象关系映射），它的作用是在关系型数据库和业务实体对象之间做一个映射  
优点：摆脱复杂的SQL操作，适应快速开发，让数据结果变得简单，数据库迁移成本更低  
缺点：性能较差，不适用于大型应用，复杂的SQL操作还需要通过SQL语句实现  

## 12.自定义表单认证
自定义Form组件验证表单数据  
obj.cleaned_data  


# 三、前端js知识
## 1.jsonp
浏览器的同源策略：同协议、域名、端口，浏览器给其它域名发送请求，服务端也返回了数据，但是浏览器不给于显示  
jsonp通过img、script、ifram等的src属性发送get请求进行跨域，返回需要的数据  

## 2.ajax
AJAX = 异步 JavaScript 和 XML。  
AJAX 是一种用于创建快速动态网页的技术。  
通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。  
这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新  

## 3.文件上传和下载
<input type="file" id="files" multiple>  
python后端：  
```python
file_obj = request.POST.get('files')
with open(file_path,'wb') as f:
	for chunk in file_obj.chunks():
		f.write(chunk)
```  

## 4.this
this 指的是当前对象   
在函数外（顶级作用域中）：在浏览器中this 指的是全局对象。  

## 5.当浏览器敲下URL后会发生什么
1.浏览器把URL发到DNS服务器进行解析出IP和端口  
2.浏览器拿到IP和端口后通过TCP的三次握手协议进行建立连接  
3.请求数据封装在第三次握手的确认请求中  
4.服务器给浏览器返回相关数据  
5.服务器发起请求进行断开连接  
6.浏览器拿到数据后进行渲染到页面中。  

## 6.页面优化
1. 减少 HTTP请求数
(1).从设计实现层面简化页面（像百度搜索页面）  
(2). 合理设置 HTTP缓存  
(3). 资源合并与压缩，如果可以的话，尽可能的将外部的脚本、样式进行合并，多个合为一个。  
2.将外部脚本置底（将脚本内容在页面信息内容加载后再加载）  
3.异步执行 inline脚本(其实原理和上面是一样，保证脚本在页面内容后面加载。)  
4.Lazy Load Javascript（只有在需要加载的时候加载，在一般情况下并不加载信息内容。）  
5.将 CSS放在 HEAD中  
6.异步请求 Callback（就是将一些行为样式提取出来，慢慢的加载信息的内容）  
7.减少不必要的 HTTP跳转  
8.避免重复的资源请求  

## 7.如何让你修改的前端页面立即在客户端生效
修改文件名

# 四、网络编程
## 1.让程序实现高并发的方案有哪些
一，Nginx要做负载均衡   
二，程序层面做多线程，锁等机制   
三，数据库层面处理   
四，服务器配置要尽量高   
五，可能还有其他的方案  

## 2.进程
进程：是资源管理单位，进行是相互独立的，实现并行和并发（并行是并发的一种）  
多进程：多进程模块multiprocessing来实现，cpu密集型，计算型IO可以用多进程  

## 3.线程
线程：是最小的执行单位，线程的出现为了降低上下文切换的消耗，提供系统的并发性  
多线程：多线程模块threading来实现，IO密集型（输入输出读取写入），多线程可以提高效率  


## 4.协程
协程：依赖于geenlet，对于多线程应用。cpu通过切片的方式来切换线程间的执行，遇到IO操作自动切换，线程切换时需要耗时，  
而协成好处没有切换的消耗，没有锁定概念。  

## 5.IO多路复用/异步非阻塞
IO多路复用：通过一种机制，可以监听多个描述符 select/poll/epoll  
select：连接数受限，查找配对速度慢，数据由内核拷贝到用户态  
poll：改善了连接数，但是还是查找配对速度慢，数据由内核拷贝到用户态  
epoll：epoll是linux下多路复用IO接口，是select/poll的增强版，它能显著提高程序在大量并发连接中只有少量活跃的情况下的系统CPU利用率  
异步非阻塞：异步体现在回调上，回调就是有消息返回时告知一声儿进程进行处理。非阻塞就是不等待，不需要进程等待下去，继续执行其他操作，不管其他进程的状态。  

## 6.用户态、内核态
内核从本质上看是一种软件——控制计算机的硬件资源，并提供上层应用程序运行的环境。  
用户态即上层应用程序的活动空间，应用程序的执行必须依托于内核提供的资源，包括CPU资源、存储资源、I/O资源等。  
## 7.队列
队列，用来在生产者和消费者线程之间的信息传递  
FIFO即First in First Out,先进先出。  
```python
import Queue

q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
```
LIFO即Last in First Out,后进先出。  
优先级队列  

## 8.Redis缓存
支持五大数据类型：string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）  
支持持久化  

# 五、数据库
## 1.索引原理
B+树：9-30下有三个指针表示P1小于9的、P2在9到30之内的、P3大于30的  
在P2的时候使用二分查找，速度很快。  

## 2.外键
一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY。

## 3.关联查询
left join ...on; right join ... on ;full join ... on
  
## 4.存储过程、事务
存储过程是一个SQL语句集合，当主动去调用存储过程时，其中内部的SQL语句会按照逻辑执行。　　
存储过程不允许执行return语句，但是可以通过out参数返回多个值，存储过程一般是作为一个独立的部分来执行，  
存储过程是一个预编译的SQL语句。  

## 5.数据库优化的一些方法
select句中避免使用 '*'  
减少访问数据库的次数  
删除重复记录  
用where子句替代having子句  
减少对表的查询  
explain显示了mysql如何使用索引来处理select语句以及连接表。可以帮助选择更好的索引和写出更优化的查询语句。  

# 六、算法
## 1.冒泡
```python
#Python的冒泡排序
alist = [1,4,7,3,6,9,5]   
def func(alist): 
    for item in range(len(alist)-1,0,-1):  
        for i in range(item): 
            if alist[i]>alist[i+1]:     # 如果前一个数(a)比后一个数(b)大
                mid = alist[i]          # 把大数赋给中间变量(mid)
                alist[i] = alist[i+1]   # 把b(小数)放在前一个数(a)大数的位置上 
                alist[i+1] = mid        # 把中间变量存的大数放在b的位置上 完成一次排序
    return alist
```  

## 2.二分
```python
# 二分查找 必须是有序数列
List = [5, 7, 25, 28, 30, 55, 63, 99,102,109,160,199,200]
def func(List,L):
    count = 0
    while True:
        mid = len(List)//2
        if len(List)==1 and List[0]!=L:
            print('你查找的数不在列表范围内')
            break
        elif L>List[mid]:
            count+=1
            print('第%s次查找，所猜的值是%s,中间值是%s,现在要去区间%s找'%(count,L,mid,List[mid:]))
            List = List[mid:]
            print(List)
        elif L<List[mid]:
            count+=1
            print('第%s次查找，所猜的值是%s,中间值是%s,现在要去区间%s找'%(count,L,mid,List[:mid]))
            List = List[:mid]
            print(List)
        elif L == List[mid]:
            count+=1
            print('第%s次查找，所猜的值是%s,恭喜你找到了！'%(count,L))
            break
func(List,7)
```  

## 3.快排
```python
import time,random

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr)<1:
        return arr
    else:
        pivolt = arr[0]        # 取数组中的第一个元素
        for i in arr:
            if i < pivolt:     # 如果第二个元素小于第一个元素
                less.append(i) # 把第二个小的元素加入less列表
            elif i > pivolt:   # 如果第二个元素大于第一个元素
                more.append(i) # 把第二个大的元素加入more列表
            else:
                pivotList.append(i) # 相等就加入picotList列表

        less = quickSort(less)
        more = quickSort(more)
        return  less + pivotList + more

start = time.time()
res = [ i for i in range(100000)]
random.shuffle(res)
res = quickSort(res)
stop = time.time()
print(stop-start)    # 1.4870026111602783
```  

## 4.堆排序
```python
def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst
```  
## 5.工厂方法
1.简单工厂模式:父类规定必须要继承的方法，父类自己不实现，子类需要继承该方法。  
2.工厂方法模式:定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类。  
3.抽象工厂模式:定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。  


# 七、开发工具git
## 1.git
git status //查看工作区状态  
git add .                       #提交所有文件   
git commit -m "自定义提交信息"  #提交注释    
git ls-files       #仅查看所有的文件名  
git log    //显示操作日志  
git reflog //查看所有的日志  
git reset --hard 版本号  #从分支回到原文件  
git rm test.txt  # 删除文件  
git commit -m "remove test.txt"　
git stash #临时保存现在写的代码  
git branch       #查看所有分支  
git branch dev   #创建dev分支  
git checkout dev #切换到dev分支  
git checkout bug #切换到bug分支  
git checkout master #切换到master分支，然后合并bug分支  
git merge bug  #合并分支
git push origin master  # 把master分支推送到GitHub上  

## 2.bug管理
jira:bug管理、mantis、bugzilla  
	
##3.开发部署
jekins、bamboo  
## 4.生产环境部署
nginx + django + uwsgi  
# 八、其它
## 1.爬虫
[爬虫](http://www.cnblogs.com/guotianbao/category/1123946.html)
## 2.tornado
[tornado](http://www.cnblogs.com/wupeiqi/articles/5341480.html)
## 3.flask
[flask](http://www.cnblogs.com/wupeiqi/articles/5341480.html)	
	
## Linux常用命令	
[Linux常用命令](http://www.cnblogs.com/guotianbao/p/7908032.html)	

## restful API
[restful API](http://www.cnblogs.com/guotianbao/p/8547768.html)  

[老男孩Python师兄面试题整理](http://www.cnblogs.com/guotianbao/p/8631395.html)  	
[Python面试题](http://www.cnblogs.com/guotianbao/p/8182787.html)  	
[python面试题2017](http://www.cnblogs.com/guotianbao/p/7902691.html)  	
[python面试题的知识点](http://www.cnblogs.com/guotianbao/p/7894465.html)  

	
	
	
	
	
	