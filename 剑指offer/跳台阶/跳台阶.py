'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        #if number <=1:
        #    return 1
        '''
        如果是从第n-2个台阶跳上来
        如果是从第n-1个台阶跳上来
        那么第n个台阶跳上来的方法是n-1的方法加上n-2的方法
        关键是需要确定从哪开始返回
        这种方式时间复杂度高，容易超时
        还有一种思路，动态规划
        或者看做裴波拉切数列
        '''

        #n_method = self.jumpFloor(number-1) + self.jumpFloor(number-2)
        #return n_method
        if number <2:
            return 1
        a = [1,1]
        for i in range(2,number+1):
            a.append(a[i-1] + a[i-2])
        return a[i]


if __name__ == "__main__":
    solu = Solution()
    print(solu.jumpFloor(4))