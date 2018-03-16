# 二分查找只能对排好序的List列表进行查找
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
            print('第%s次查找，所猜的值是%s,中间值是%s,现在要去区间%s找'%(count,L,List[mid],List[mid:]))
            List = List[mid:]
            print(List)
        elif L<List[mid]:
            count+=1
            print('第%s次查找，所猜的值是%s,中间值是%s,现在要去区间%s找'%(count,L,List[mid],List[:mid]))
            List = List[:mid]
            print(List)
        elif L == List[mid]:
            count+=1
            print('第%s次查找，所猜的值是%s,恭喜你找到了！'%(count,L))
            break
func(List,102)








