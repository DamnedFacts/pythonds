# -*- coding: utf-8 -*-
""" A simple Queue ADT using a list as a data structure

Originally written by:
    Bradley N. Miller, David L. Ranum
    Introduction to Data Structures and Algorithms in Python
    Copyright 2005

Updated by:
    Richard Sarkis <rich@sark.is>

"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
