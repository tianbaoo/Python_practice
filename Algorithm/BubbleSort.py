alist = [1,47,9,3,22,5]
def func(alist):
    for item in range(len(alist)-1,0,-1):
	    for i in range(item):
		    if alist[i]>alist[i+1]:
			    mid = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = mid
	return alist
	    









