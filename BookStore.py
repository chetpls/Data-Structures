import sys

import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time
import MaxQueue


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = SLLQueue.SLLQueue()
        self.indexTitle = ChainedHashTable.ChainedHashTable()
        self.indexSortedTitle = None
        self.bestSellers = BinaryHeap.BinaryHeap()

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        self.indexSortedTitle = BinarySearchTree.BinarySearchTree()
        with open(fileName, encoding="UTF-8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                b = s
                self.indexTitle.add(title, b)
                self.indexSortedTitle.add(title, b)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def getBestSeller(self):
        maxS = MaxQueue.MaxQueue()
        for k in self.shoppingCart:
            maxS.add(k)
        print(maxS.max())

    def kBestSeller(self, infix, k):

        for book in range(self.bookCatalog.size()):
            x = self.bookCatalog.get(book)
            if infix in x.title:
                x.rank = (x.rank * -1)
                self.bestSellers.add(x)
        for i in range(k):
            print(self.bestSellers.find_min().rank *-1, self.bestSellers.remove().title)

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        count = 0
        for k in range(self.bookCatalog.size()):
            if count < 50:
                if infix in self.bookCatalog.get(k).title:
                    print(self.bookCatalog.get(k).key, self.bookCatalog.get(k).title)
                    count += 1
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"Removed from shopping cart {u} Completed in {elapsed_time} seconds")

    def reverseShoppingCart(self):
        self.shoppingCart.reverse()

    def searchByIndexTitle(self, title: str):
        if self.indexTitle.find(title) is not None:
            self.shoppingCart.add(title)
            print(f"{self.indexTitle.find(title)} has been added to shopping cart")
        else:
            print(f"The book with title, {title}, is not found")

    def searchByPrefix(self, prefix: str):
        pref = self.indexSortedTitle.find(prefix)
        if pref is not None:
            self.shoppingCart.add(pref)
            print(f"{pref} has been added to shopping cart")
        else:
            print(f"Book with prefix {prefix} not found")

    def printShoppingCart(self):
        index = self.shoppingCart.j
        for i in range(index, self.shoppingCart.size() + index):
            print(self.shoppingCart.a[i])

    def printBookCatalog(self):
        for i in range(self.bookCatalog.size() - 1):
            print(self.bookCatalog.get(i))
