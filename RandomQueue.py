import numpy as np
import random 
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> np.object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo

        random_element = random.randint(0, self.n-1)
        temp = self.a[0]
        self.a[0] = self.a[random_element]
        self.a[random_element] = temp
        return super().remove()


