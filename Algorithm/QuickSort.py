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