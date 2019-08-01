"""
author: buppter
datetime: 2019/8/1 20:46

题目描述：
验证二叉搜索树
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


示例：
    2
   / \
  1   3

Input: [2,1,3]
Output: true

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

解题思路：
1. 中序遍历，只要满足数组为升序，即为二叉搜索树
2. 找到左子树最大的值 max，右子树最小的值 min，只要满足 max < root < min，即为二叉搜索树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        if inorder == list(sorted(set(inorder))):
            return True
        return False

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
