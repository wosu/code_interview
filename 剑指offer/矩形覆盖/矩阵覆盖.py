'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
问题分析：
一个2*n的矩阵，用2*1的去填充：
首先2*1的填充有两种方式：横放和竖直放，那就分两种情况取讨论
如果竖直放：则将2*n的矩形分成了两部分：2*1和2*(n-1)
如果横着放：则将2*n的矩形分成了三部分：1*2,1*2,2*(n-2)
            注意这里n>=3
那么2*n的矩形就分解成
2*n=2*(n-1) + 2*(n-2);接着在求2*(n-1)有多少种和2*(n-2)有多少种
有点类似裴波拉切数列
那么求解有两种方式：
1.最直接的递归，但时间复杂度高
2.贪心和dp
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number<=2:
            return number
        arra = [1,2]
        for i in range(2,number):
            arra.append(arra[i-1] + arra[i-2])
        return arra[i]


if __name__ == '__main__':
    solu = Solution()
    print(solu.rectCover(5))




