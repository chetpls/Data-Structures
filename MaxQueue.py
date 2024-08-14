from DLList import DLList
from SLLQueue import SLLQueue
import numpy as np


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.deque = DLList()

    def add(self, x: np.object):
        super().add(x)
        if self.deque.size() == 0:
            self.deque.add(0, x)
        else:
            while self.deque.size() != 0 and self.deque.dummy.prev.x < x:
                self.deque.remove(self.deque.n-1)
            self.deque.add(self.deque.n, x)

    def remove(self) -> np.object:
        if self.n == 0:
            return None
        if self.head.x == self.deque.dummy.next.x:
            self.deque.remove(0)
        return super().remove()

    def max(self) -> np.object:
        if self.deque.size() == 0:
            return None
        return self.deque.dummy.next.x
