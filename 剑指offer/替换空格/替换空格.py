'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        str1 = []
        for i in range(0,len(s)):
            if len(s[i].strip()) ==0:
                str1.append("%20")
            else:
                str1.append(s[i])
        return "".join(str1)


if __name__ == '__main__':
    a = "We Are Happy"
    s = Solution()
    print(s.replaceSpace(a))
