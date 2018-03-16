"""
题目描述：写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。

样例：

给出 s = "abcd"，t="dcab"，返回 true.

给出 s = "ab", t = "ab", 返回 true.

给出 s = "ab", t = "ac", 返回 false.
"""

class AnagramDetection:
    # 1.先对两个字符串进行list化
	# 2.对字符串对应的两个list进行排序
	# 3.依次比较字符是否匹配
	def anagramSolution1(self,s1,s2):
	    alist1 = list(s1)
	    alist2 = list(s2)
		
		alist1.sort()
		alist2.sort()
		
		if alist1 == alist2:
            return True
        else:
            return False
			
#		pos = 0
#		matches = True
		
#		while pos < len(s1) and matches:
#		    if alist1[pos] == alist2[pos]:
#			    pos += 1
#			else:
#			    matches = False
#		return matches
s1 = 'abcade'
s2 = 'acbade'
hello = AnagramDetection()
res = hello.anagramSolution1(s1,s2)
print(res)		



















