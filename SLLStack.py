from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x: np.object):
        u = self.Node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n = self.n + 1
        return x
        
    def pop(self) -> np.object:
        if self.n == 0:
            return None
        x = self.head.x
        self.head = self.head.next
        self.n = self.n - 1
        if self.n == 0:
            self.tail = None
        return x

    def size(self) -> int:
        return self.n

    def reverse(self):
        u = self.head
        v = u.next
        while v is not None:
            w = v.next
            v.next = u
            u = v
            v = w
        self.head, self.tail = self.tail, self. head
        self.tail.next = None

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
