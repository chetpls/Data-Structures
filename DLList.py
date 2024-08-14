from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i: int) -> Node:
        if i < 0 or i > self.n:
            raise IndexError()
        if i < self.size() / 2:
            node = self.dummy.next
            for j in range(i):
                node = node.next
        else:
            node = self.dummy
            for j in range(self.size() - i):
                node = node.prev
        return node
        
    def get(self, i) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: np.object) -> Node:
        if w is None:
            raise IndexError()
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n = self.n + 1
        return u
            
    def add(self, i: int, x: np.object):
        return self.add_before(self.get_node(i), x)

    def _remove(self, w: Node):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n = self.n - 1
        return w.x
    
    def remove(self, i:int):
        if i < 0 or i > self.n:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        front = self.dummy
        back = self.dummy
        count = 0

        if self.n is None:
            return True

        for e in range(self.n):
            if front.next.x == back.prev.x:
                count += 1
                front = front.next
                back = back.prev
            else:
                return False
        if count == self.n:
            return True
        else:
            return False



    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not self.dummy:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
