'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回

二叉树的遍历方式三种：前序，中序，后续
前序：根左右：先遍历根节点，在遍历左子树，在遍历右子树
中序：左根右：先遍历左子树，在遍历根节点，在遍历右子树
后序：左右根：先遍历左子树，再遍历右子树，最后遍历根节点
树的确定：
先中，后中确定一棵树；为什么需要需要中序，因为先序或者后序可以确定一棵树的根节点，
确定根节点后可以根据中序，得到树的左子树和右子树；往后递归确定一棵树

一个二叉树，砍掉连接的父节点，剩下的又相当于一个独立的二叉树
https://www.cnblogs.com/du001011/p/11229170.html
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    # 先序遍历，中序遍历
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) ==0:
            return None

        root_v = pre[0]
        root_node = TreeNode(root_v)
        root_index = tin.index(root_v)
        #根据根节点，可以知道左子树的节点数量和右子树节点数量
        left_num = root_index
        right_num = len(tin) - left_num -1

        left_tin_tree = tin[0:left_num]
        right_tin_tree = tin[left_num+1:]

        left_pre_tree = pre[1:left_num+1]
        right_pre_tree = pre[1+left_num:]

        root_node.left = self.reConstructBinaryTree(pre[1:1 + left_num], tin[0:left_num])
        root_node.right = self.reConstructBinaryTree(pre[1 + left_num:], tin[left_num + 1:])
        # root_node.left = self.reConstructBinaryTree(left_pre_tree,left_tin_tree)
        # root_node.right = self.reConstructBinaryTree(right_pre_tree,right_tin_tree)

        return  root_node

    def reConstructBinaryTree2(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        index = tin.index(root.val)
        leftNum = index
        rightNum = len(tin) - leftNum - 1
        root.left = self.reConstructBinaryTree2(pre[1:1 + leftNum], tin[0:leftNum])
        root.right = self.reConstructBinaryTree2(pre[1 + leftNum:], tin[leftNum + 1:])
        return root

pre = [1,2,4,7,3,5,6,8]
mid = [4,7,2,1,5,3,8,6]
solu = Solution()
solu.reConstructBinaryTree(pre,mid)