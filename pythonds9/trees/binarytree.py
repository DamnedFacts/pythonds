# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
#

from __future__ import print_function

class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.

    Modified to allow for trees to be constructed from other trees rather than always creating
    a new tree in the insert_left or insert_right
    """

    def __init__(self,root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self,new_node):

        if isinstance(new_node, BinaryTree):
            t = new_node
        else:
            t = BinaryTree(new_node)

        if self.left_child is not None:
            t.left = self.left_child

        self.left_child = t

    def insert_right(self,new_node):
        if isinstance(new_node,BinaryTree):
            t = new_node
        else:
            t = BinaryTree(new_node)

        if self.right_child is not None:
            t.right = self.right_child
        self.right_child = t

    def is_leaf(self):
        return ((not self.left_child) and (not self.right_child))

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self,obj):
        self.key = obj

    def get_root_val(self,):
        return self.key

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)


    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def printexp(self):
        if self.left_child:
            print('(', end=' ')
            self.left_child.printexp()
        print(self.key, end=' ')
        if self.right_child:
            self.right_child.printexp()
            print(')', end=' ')

    def postordereval(self):
        opers = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}

        res1 = None
        res2 = None
        if self.left_child:
            res1 = self.left_child.postordereval()  # // \label{peleft}
        if self.right_child:
            res2 = self.right_child.postordereval()  # // \label{peright}
        if res1 and res2:
            return opers[self.key](res1,res2)  # // \label{peeval}
        else:
            return self.key

def inorder(tree):
    if tree is None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

def printexp(tree):
    if tree.left_child:
        print('(', end=' ')
        printexp(tree.get_left_child())
    print(tree.get_root_val(), end=' ')
    if tree.right_child:
        printexp(tree.get_right_child())
        print(')', end=' ')

def printexp(tree):
    s_val = ""
    if tree:
        s_val = '(' + printexp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + printexp(tree.get_right_child()) + ')'
    return s_val

def postordereval(tree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.get_left_child())  # // \label{peleft}
        res2 = postordereval(tree.get_right_child())  # // \label{peright}
        if res1 and res2:
            return opers[tree.get_root_val()](res1,res2)  # // \label{peeval}
        else:
            return tree.get_root_val()

def height(tree):
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.left_child), height(tree.right_child))


if __name__ == '__main__':
    t = BinaryTree(7)
    t.insert_left(3)
    t.insert_right(9)
    inorder(t)
    import operator
    x = BinaryTree('*')
    x.insert_left('+')
    l = x.get_left_child()
    l.insert_left(4)
    l.insert_right(5)
    x.insert_right(7)
    print(printexp(x))
    print(postordereval(x))
    print(height(x))
