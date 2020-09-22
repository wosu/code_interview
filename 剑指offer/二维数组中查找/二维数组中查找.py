'''
题目描述
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

有序矩阵，因为从左到右递增，从上到下递增，那么意味着，
最右下角的数最大，从最右下角开始找
行数等于=len(array)
列数=len(array[0])
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) ==0:
            return False
        nrow = len(array)
        mcol = len(array[0])

        #从第最后一个元素开始，往左和往上开始查找
        row_i = nrow
        col_j = mcol

        if array[row_i-1][col_j-1] < target:
            return False
        while row_i >=1 and col_j >=1:
            a_ij = array[row_i-1][col_j-1]
            print("--",a_ij,row_i,col_j)
            if a_ij == target:
                return True
            elif a_ij < target:
                row_i -= 1
                col_j += 1
            elif a_ij > target:
                col_j -= 1
            '''
                从左往右开始往前找，当第i行所有列都找完了，且没找到，则又重新开始从
                第i-1行，最左边开始找
            '''
            if col_j == 0:
                row_i -=1
                col_j = mcol

        print(row_i,col_j)
        return False

if __name__ == '__main__':
    a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(a)
    solu = Solution()
    print(solu.Find(7,a))

