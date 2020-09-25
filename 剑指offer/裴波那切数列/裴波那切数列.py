'''
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39
特点：前面两项相加等于后面两项
即a_n = a_n_1 + a_n_2
主要考点是数组，利用数组是有顺序的特性
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n >=2:
            a0 = 0
            a1 = 1
            arra = []
            arra.append(a0)
            arra.append(a1)
            if n> 39:
                n = 39
            i = 2
            '''
            注意点，这里容易写成i<n，数列是从第0项开始
            '''
            while i< n+1:
                x = arra[i-2] + arra[i-1]
                arra.append(x)
                i += 1
            return arra[i-1]


if __name__ == '__main__':
    solu = Solution()
    # 0,1,1,2,3,5,8,13,21,34
    print(solu.Fibonacci(3))