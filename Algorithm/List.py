class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):     # 设置next等于newData
        self.next = newdata

    def setNext(self, nextNode):
        self.next = nextNode
		
temp = Node(95)
temp.setData(18)
print(temp.getNext())

# 定义一个无序链表
class UnorderedList:
    def __init__(self):
	    self.head = None            # 初始化时.head指向None
		
	def isEmpty(self):
	    return self.head == None    # 如果.head指向None,返回True,否则返回False
		
	def add(self,item):
	    temp = Node(item)           # temp是Node的实例,数据data=item
        temp.setNext(self.head)     # 传入参数self.head
		self.head = temp            # self.head是一个Node指针
		
	def size(self):
	    current = self.head         # current是一个Node指针或None
        count = 0
		while current != None:      # 当current是Node指针时
		    count += 1                   # 计数加一
			current = current.getNext()  # 拿到Node指针的下一个next值
		return count
		
    def search(self,item):
	    current = self.head         # current是一个Node指针或None
		found = False
		while current != None and not found:
		# 当current是Node指针且found==False时
		    if current.getData() == item:
			    found = True
			else:
			    current = current.getNext()
		return found
		
    def remove(self,item):
	    current = self.head         # current是一个Node指针或None
		previous = None             # 定义一个None 用来指向被移除节点的下一个节点
		found = False
		while not found:
            if current.getData() == item     # 找到要删除的值，执行下一个if语句
               found = True
            else:
                previous = current           # 把当前节点赋给previous暂存起来
                current = current.getNext()  # current更新为下一个节点，继续while循环
        if previous == None:                 # previous == None表示要删除的是第一个节点
            self.head = current.getNext()    # 直接把self.head指向下一个节点即可
        else:
            previous.setNext(current.getNext())   # 否者暂存节点previous的next值等于要删除节点的下一个next值
                                           # previous|data|next|   current|data|next|	|data|next|
                                                  #         |                                   |
                                                  #         -------------------------------------
myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(66)
myList.add(93)
myList.add(26)
myList.add(54)
print(myList.search(66))
myList.remove(54)
print(myList.search(54))































