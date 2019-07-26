# -*- coding: utf-8 -*-
""" A simple Stack ADT using a list as a data structure

Originally written by:
    Bradley N. Miller, David L. Ranum
    Introduction to Data Structures and Algorithms in Python
    Copyright 2005

Updated by:
    Richard Sarkis <rich@sark.is>

"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
