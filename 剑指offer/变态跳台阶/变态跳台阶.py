'''
一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

a_n=a_0+a_1+....+a_n_1
本质是在原来跳台阶基础上增加了一层
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=1:
            return 1
        arra = [1,1]
        for i in range(2,number+1):
            a_i = 0
            for j in range(0,i):
                a_i += arra[j]
            arra.append(a_i)

        return arra[i]

if __name__ == '__main__':
    solu = Solution()
    print(solu.jumpFloorII(2))