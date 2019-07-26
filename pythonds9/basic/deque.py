# -*- coding: utf-8 -*-
""" A simple Deque ADT using a list as a data structure

Originally written by:
    Bradley N. Miller, David L. Ranum
    Introduction to Data Structures and Algorithms in Python
    Copyright 2005

Updated by:
    Richard Sarkis <rich@sark.is>

"""


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
