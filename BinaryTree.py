from Queue import *
from BinaryTreePrinter import *


class TreeNode:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)

        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.dequeue()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.right)
                    nodes.enqueue(checking_node.left)

    def __str__(self):
        TreePrinter = BinaryTreePrinter()
        return TreePrinter.get_tree_string(self.root)


m_t = BinaryTree()

for c in ['a','b','c']:
    m_t.insert(c)
    print(m_t)
