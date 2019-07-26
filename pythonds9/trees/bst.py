#!/bin/env python3.1
# Bradley N. Miller,  David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005,  2010
# 

import unittest
class BinarySearchTree:
    '''
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
                  items() 
                  keys() 
                  values()
                  put(k, v)
                  in
                  del <==> 
    '''

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        if self.root:
            self._put(key, val,self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self,  k,  v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,  key,  current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError('Error,  key not in tree')


    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key,self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size-1
            else:
                raise KeyError('Error,  key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error,  key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf(): #leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children(): #interior
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else: # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                       current_node.left_child.payload,
                                       current_node.left_child.left_child,
                                       current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                       current_node.right_child.payload,
                                       current_node.right_child.left_child,
                                       current_node.right_child.right_child)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tree):
        if tree != None:
            self._inorder(tree.left_child)
            print(tree.key)
            self._inorder(tree.right_child)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self,  tree):
        if tree:
            self._postorder(tree.right_child)
            self._postorder(tree.left_child)
            print(tree.key)

    def preorder(self):
        self._preorder(self,self.root)

    def _preorder(self, tree):
        if tree:
            print(tree.key)
            self._preorder(tree.left_child)
            self._preorder(tree.right_child)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balanceFactor = 0

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ


    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def __iter__(self):
        """The standard inorder traversal of a binary tree."""
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def testgetput(self):
        print('testgetput')
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        print(self.bst.get(50))
        assert self.bst.get(50) == 'a'
        assert self.bst.get(45) == 'f'
        assert self.bst.get(85) == 'd'
        assert self.bst.get(10) == 'b'
        assert self.bst.root.key == 50
        assert self.bst.root.left_child.key == 10
        assert self.bst.root.right_child.key == 70

    def testputoper(self):
        print('testputoper')
        self.bst[25] = 'g'
        assert self.bst[25] == 'g'

    def test_find_succ(self):
        print('testing findSucc')
        x = BinarySearchTree()
        x.put(10, 'a')
        x.put(15, 'b')
        x.put(6, 'c')
        x.put(2, 'd')
        x.put(8, 'e')
        x.put(9, 'f')
        assert x.root.left_child.left_child.find_successor().key == 6
        assert x.root.left_child.right_child.find_successor().key == 9
        assert x.root.left_child.right_child.right_child.find_successor().key == 10

    def test_size(self):
        print('testing testSize')
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        assert self.bst.length() == 7

    def test_delete(self):
        print('testing delete')
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.bst.put(5, 'g')
        print('initial inorder')
        self.bst.inorder()
        assert (10 in self.bst) is True
        self.bst.delete_key(10)
        print('delete 10 inorder')
        self.bst.inorder()
        assert (10 in self.bst) is False
        assert self.bst.root.left_child.key == 15
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        assert self.bst.get(30) == 'd'
        self.bst.delete_key(15)
        print('delete 15 inorder')
        self.bst.inorder()
        assert self.bst.root.left_child.key == 30
        assert self.bst.root.left_child.right_child.key == 45
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        self.bst.delete_key(70)
        print('delete 70 inorder')
        self.bst.inorder()
        assert (85 in self.bst) is True
        assert self.bst.get(30) == 'd'
        print('root key = ',  self.bst.root.key)
        print('left = ',self.bst.root.left_child.key)
        print('left left = ',self.bst.root.left_child.left_child.key)
        print('left right = ',self.bst.root.left_child.right_child.key)
        print('right = ',self.bst.root.right_child.key)
        self.bst.delete_key(50)
        assert self.bst.root.key == 85
        assert self.bst.root.left_child.key == 30
        assert self.bst.root.right_child is None
        assert self.bst.root.left_child.left_child.key == 5
        assert self.bst.root.left_child.right_child.key == 45
        assert self.bst.root.left_child.left_child.parent == self.bst.root.left_child
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        print('new root key = ',  self.bst.root.key)
        self.bst.inorder()
        self.bst.delete_key(45)
        assert self.bst.root.left_child.key == 30
        self.bst.delete_key(85)
        assert self.bst.root.key == 30
        print('xxxx ',self.bst.root.left_child.parent.key,  self.bst.root.key)
        assert self.bst.root.left_child.parent == self.bst.root
        self.bst.delete_key(30)
        assert self.bst.root.key == 5
        self.bst.inorder()
        print("final root = " + str(self.bst.root.key))
        assert self.bst.root.key == 5
        self.bst.delete_key(5)
        assert self.bst.root is None

    def test_del2(self):
        self.bst.put(21,  'a')
        self.bst.put(10,  'b')
        self.bst.put(24,  'c')
        self.bst.put(11,  'd')
        self.bst.put(22,  'd')
        self.bst.delete_key(10)
        assert self.bst.root.left_child.key == 11
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.right_child.key == 24
        self.bst.delete_key(24)
        assert self.bst.root.right_child.key == 22
        assert self.bst.root.right_child.parent == self.bst.root
        self.bst.delete_key(22)
        self.bst.delete_key(21)
        print("del2 root = ",self.bst.root.key)
        assert self.bst.root.key == 11
        assert self.bst.root.left_child is None
        assert self.bst.root.right_child is None

    def test_large(self):
        import random
        print('testing a large random tree')
        i = 0
        rand_list = []
        while i < 10000:
            nrand = random.randrange(1, 10000000)
            if nrand not in rand_list:
                rand_list.append(nrand)
                i += 1
        print(rand_list)
        for n in rand_list:
            self.bst.put(n, n)
        sort_list = rand_list[:]
        sort_list.sort()
        random.shuffle(rand_list)
        for n in rand_list:
            min_node = self.bst.root.find_min()
            if min_node:
                assert min_node.key == sort_list[0]
            root_pos = sort_list.index(self.bst.root.key)
            succ = self.bst.root.find_successor()
            if succ:
                assert succ.key == sort_list[root_pos+1]
            else:
                assert self.bst.root.right_child == None
            self.bst.delete_key(n)
            sort_list.remove(n)
            
        assert self.bst.root == None

    def test_iter(self):
        import random
        i = 0
        rand_list = []
        while i < 100:
            nrand = random.randrange(1, 10000)
            if nrand not in rand_list:
                rand_list.append(nrand)
                i += 1
        for n in rand_list:
            self.bst.put(n, n)
        sort_list = rand_list[:]
        sort_list.sort()

        i = 0
        for j in self.bst:
            assert j == sort_list[i]
            i += 1
# the following exercises all of the branches in deleting a node with one child
    def test_case1(self):
        self.bst.put(10, 10)
        self.bst.put(7, 7)
        self.bst.put(5, 5)
        self.bst.put(1, 1)
        self.bst.put(6, 6)
        self.bst.delete_key(7)
        assert self.bst.root.left_child.key == 5
        assert self.bst.root == self.bst.root.left_child.parent
        assert self.bst.root.left_child.left_child.key == 1
        assert self.bst.root.left_child.right_child.key == 6

    def test_case2(self):
        self.bst = BinarySearchTree()
        self.bst.put(10, 10)
        self.bst.put(15, 15)
        self.bst.put(12, 12)
        self.bst.put(11, 11)
        self.bst.put(13, 13)
        self.bst.delete_key(15)
        assert self.bst.root.right_child.key == 12
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.right_child.left_child.key == 11
        assert self.bst.root.right_child.right_child.key == 13

    def test_case3(self):
        self.bst = BinarySearchTree()
        self.bst.put(10, 10)
        self.bst.put(6, 6)
        self.bst.put(8, 8)
        self.bst.put(7, 7)
        self.bst.put(9, 9)
        self.bst.delete_key(6)
        assert self.bst.root.left_child.key == 8
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.left_child.left_child.key == 7
        assert self.bst.root.left_child.right_child.key == 9

    def test_case4(self):
        self.bst = BinarySearchTree()
        self.bst.put(10, 10)
        self.bst.put(15, 15)
        self.bst.put(20, 20)
        self.bst.put(17, 17)
        self.bst.put(22, 22)
        self.bst.delete_key(15)
        assert self.bst.root.right_child.key == 20
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.right_child.right_child.key == 22
        assert self.bst.root.right_child.left_child.key == 17

    def test_case5(self):
        self.bst.put(10, 10)
        self.bst.put(20, 20)
        self.bst.put(17, 17)
        self.bst.put(22, 22)
        self.bst.delete_key(10)
        assert self.bst.root.key == 20
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.left_child.key == 17
        assert self.bst.root.right_child.key == 22

    def test_case6(self):
        self.bst.put(10, 10)
        self.bst.put(5, 5)
        self.bst.put(1, 1)
        self.bst.put(7, 7)
        self.bst.delete_key(10)
        assert self.bst.root.key == 5
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.left_child.key == 1
        assert self.bst.root.right_child.key == 7

    def test_bad_delete(self):
        self.bst.put(10, 10)
        with self.assertRaises(KeyError):
            self.bst.delete_key(5)
        self.bst.delete_key(10)
        with self.assertRaises(KeyError):
            self.bst.delete_key(5)


if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()

### Local Variables:
### End:
