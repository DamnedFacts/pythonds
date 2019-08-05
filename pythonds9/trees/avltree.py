# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005, 2010
# 

import unittest
from .bst import BinarySearchTree, TreeNode


class AVLTree(BinarySearchTree):
    """
    Author:  Brad Miller
    Date:  1/15/2005
    Description:  Imlement a binary search tree with the following interface
                  functions:
                  __contains__(y) <==> y in x
                  __getitem__(y) <==> x[y]
                  __init__()
                  __len__() <==> len(x)
                  __setitem__(k, v) <==> x[k] = v
                  clear()
                  get(k)
                  has_key(k)
                  items()
                  keys()
                  values()
                  put(k, v)
    """

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val,
                                                   parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val,
                                                    parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                # Do an LR Rotation
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                # single left
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                # Do an RL Rotation
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                # single right
                self.rotate_right(node)

    def rotate_left(self, rot_root):
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.left_child is None:
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = (rot_root.balance_factor + 1 -
                                   min(new_root.balance_factor, 0))
        new_root.balance_factor = (new_root.balance_factor + 1 +
                                   max(rot_root.balance_factor, 0))

    def rotate_right(self, rot_root):
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child is None:
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = (rot_root.balance_factor - 1 -
                                   max(new_root.balance_factor, 0))
        new_root.balance_factor = (new_root.balance_factor - 1 +
                                   min(rot_root.balance_factor, 0))


class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = AVLTree()

    def test_auto1(self):
        self.bst.put(30, 'a')
        self.bst.put(50, 'b')
        self.bst.put(40, 'c')
        assert self.bst.root.key == 40

    def test_auto2(self):
        self.bst.put(50, 'a')
        self.bst.put(30, 'b')
        self.bst.put(40, 'c')
        assert self.bst.root.key == 40

    def test_auto3(self):
        self.bst.put(50, 'a')
        self.bst.put(30, 'b')
        self.bst.put(70, 'c')
        self.bst.put(80, 'c')
        self.bst.put(60, 'd')
        self.bst.put(90, 'e')
        assert self.bst.root.key == 70

    def test_auto4(self):
        self.bst.put(40, 'a')
        self.bst.put(30, 'b')
        self.bst.put(50, 'c')
        self.bst.put(45, 'd')
        self.bst.put(60, 'e')
        self.bst.put(43, 'f')
        assert self.bst.root.key == 45
        assert self.bst.root.left_child.key == 40
        assert self.bst.root.right_child.key == 50
        assert self.bst.root.balance_factor == 0
        assert self.bst.root.left_child.balance_factor == 0
        assert self.bst.root.right_child.balance_factor == -1

    def test_auto5(self):
        self.bst.put(40, 'a')
        self.bst.put(30, 'b')
        self.bst.put(50, 'c')
        self.bst.put(10, 'd')
        self.bst.put(35, 'e')
        self.bst.put(37, 'f')
        assert self.bst.root.key == 35
        assert self.bst.root.left_child.key == 30
        assert self.bst.root.right_child.key == 40
        assert self.bst.root.balance_factor == 0
        assert self.bst.root.left_child.balance_factor == 1
        assert self.bst.root.right_child.balance_factor == 0


if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()
