# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
import unittest

# this implementation of binary heap takes key value pairs,
# we will assume that the keys are all comparable

class PriorityQueue:
    def __init__(self):
        self.heap_array = [(0,0)]
        self.current_size = 0

    def build_heap(self,alist):
        self.current_size = len(alist)
        self.heap_array = [(0,0)]
        for i in alist:
            self.heap_array.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.perc_down(i)
            i = i - 1
                        
    def perc_down(self,i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_array[i][0] > self.heap_array[mc][0]:
                tmp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[mc]
                self.heap_array[mc] = tmp
            i = mc
                
    def min_child(self,i):
        if i*2 > self.current_size:
            return -1
        else:
            if i*2 + 1 > self.current_size:
                return i*2
            else:
                if self.heap_array[i*2][0] < self.heap_array[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def perc_up(self,i):
        while i // 2 > 0:
            if self.heap_array[i][0] < self.heap_array[i//2][0]:
               tmp = self.heap_array[i//2]
               self.heap_array[i//2] = self.heap_array[i]
               self.heap_array[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heap_array.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def del_min(self):
        retval = self.heap_array[1][1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_array.pop()
        self.perc_down(1)
        return retval
        
    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def decrease_key(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to 
        # decrease by looking at its value
        done = False
        i = 1
        my_key = 0
        while not done and i <= self.current_size:
            if self.heap_array[i][1] == val:
                done = True
                my_key = i
            else:
                i = i + 1
        if my_key > 0:
            self.heap_array[my_key] = (amt, self.heap_array[my_key][1])
            self.perc_up(my_key)
            
    def __contains__(self,vtx):
        for pair in self.heap_array:
            if pair[1] == vtx:
                return True
        return False
        
class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.the_heap = PriorityQueue()
        self.the_heap.add((2,'x'))
        self.the_heap.add((3,'y'))
        self.the_heap.add((5,'z'))
        self.the_heap.add((6,'a'))
        self.the_heap.add((4,'d'))


    def test_insert(self):
        assert self.the_heap.current_size == 5

    def test_del_min(self):
        assert self.the_heap.del_min() == 'x'
        assert self.the_heap.del_min() == 'y'
    
    def test_dec_key(self):
        self.the_heap.decrease_key('d', 1)
        assert self.the_heap.del_min() == 'd'
        
if __name__ == '__main__':
    unittest.main()
