# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
import unittest

# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0


    def build_heap(self,alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        print(len(self.heap_list), i)
        while (i > 0):
            print(self.heap_list, i)
            self.perc_down(i)
            i = i - 1
        print(self.heap_list,i)
                        
    def perc_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self,i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_up(self,i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2
 
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval
        
    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

class FooThing:
    def __init__(self,x,y):
        self.key = x
        self.val = y
        

    def __lt__(self,other):
        if self.key < other.key:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False
        
    def __hash__(self):
        return self.key

class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.the_heap = BinHeap()
        self.the_heap.insert(FooThing(5, 'a'))                               
        self.the_heap.insert(FooThing(9, 'd'))                  
        self.the_heap.insert(FooThing(1, 'x'))
        self.the_heap.insert(FooThing(2, 'y'))
        self.the_heap.insert(FooThing(3, 'z'))

    def test_insert(self):
        assert self.the_heap.current_size == 5

    def test_del_min(self):
        assert self.the_heap.del_min().val == 'x'
        assert self.the_heap.del_min().val == 'y'
        assert self.the_heap.del_min().val == 'z'
        assert self.the_heap.del_min().val == 'a'

    def test_mixed(self):
        my_heap = BinHeap()
        my_heap.insert(9)
        my_heap.insert(1)
        my_heap.insert(5)
        assert my_heap.del_min() == 1
        my_heap.insert(2)
        my_heap.insert(7)
        assert my_heap.del_min() == 2
        assert my_heap.del_min() == 5

    def test_dupes(self):
        my_heap = BinHeap()
        my_heap.insert(9)
        my_heap.insert(1)
        my_heap.insert(8)
        my_heap.insert(1)
        assert my_heap.current_size == 4
        assert my_heap.del_min() == 1
        assert my_heap.del_min() == 1
        assert my_heap.del_min() == 8

    def test_build_heap(self):
        my_heap = BinHeap()
        my_heap.build_heap([9, 5, 6, 2, 3])
        f = my_heap.del_min()
        print("f = ", f)
        assert f == 2
        assert my_heap.del_min() == 3
        assert my_heap.del_min() == 5
        assert my_heap.del_min() == 6
        assert my_heap.del_min() == 9                        


if __name__ == '__main__':
    d = {}
    d[FooThing(1,'z')] = 10
    unittest.main()
