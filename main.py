import sys

import BinarySearchTree
import BinaryTree
import Calculator
import BookStore
import DLList



def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Introduce mathematical expression
        2 Introduce variable and value
        3 Print mathematical expression
        4 Evaluation mathematical expression
        0 Return to main menu
        """)
        option = input()

        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        if option == "2":
            setVar = input("Enter variable to the expression: ")
            setVal = float(input("Enter a value for the variable: "))
            calculator.set_variable(setVar, setVal)
        if option == "3":
            newexpr = ""
            for char in expression:
                if char.isalpha():
                    newexpr += str(calculator.dict.find(char))
                else:
                    newexpr += str(char)
            print(f"{newexpr} is the new expression")
        if option == "4":
            exp = input("Introduce the expression: ")
            ans = (calculator.evaluate(exp))
            print(f" {newexpr} = {ans}")
        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Reverse Shopping Cart
        7 Print Best Selling
        8 Search book by title
        9 Search book by prefix
        10 Search infix by best seller
        0 Return to main menu
        """)
        option=input() 
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option == "6":
            bookStore.reverseShoppingCart()
        elif option == "7":
            bookStore.getBestSeller()
        elif option == "8":
            title = input("Introduce the title to search: ")
            bookStore.searchByIndexTitle(title)
        elif option == "9":
            prefix = input("Introduce Prefix:")
            bookStore.searchByPrefix(prefix)
        elif option == "10":
            infix = input("Introduce Infix: ")
            k = int(input("introduce Range: "))
            bookStore.kBestSeller(infix, k)
        ''' 
        Add the menu options when needed
        '''


def menu_test_palindrome():
    str = input("Input string here:")
    dll = DLList()
    for char in str:
        dll.append(char)
    if dll.isPalindrome():
        print(str, " is a palindrome")
    else:
        print(str, "is not a palindrome")


def menu_traversals():
    bst = BinarySearchTree.BinarySearchTree()
    option = ""
    while option != "0":
        print("""
        1 Add
        2 remove
        3 Find
        4 Height
        5 In Order
        6 Pre Order
        7 Post Order
        8 Breath First
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            num1 = input("1st input: ")
            num2 = input("2nd input: ")
            bst.add(num1, num2)
            print(f"Added ({num1}, {num2})")
        elif option == "2":
            bst.remove(input("Remove: "))
            print("removed")
        elif option == "3":
            print(bst.find(input("Find ")))
        elif option == "4":
            print(bst.height())
        elif option == "5":
            if bst is not None:
                with open("books.in_order.txt", "w") as f:
                    old_std_out = sys.stdout
                    sys.stdout = f
                    print("In Order Traversal")
                    print(bst.in_order(bst.r, []))
                    sys.stdout = old_std_out
                print(f"{bst.in_order(bst.r, [])} displayed in new text file")
        elif option == "6":
            if bst is not None:
                with open("books.pre_order.txt", "w") as f:
                    old_std_out = sys.stdout
                    sys.stdout = f
                    print("Pre Order Traversal")
                    print(bst.pre_order(bst.r, []))
                    sys.stdout = old_std_out
                print(f"{bst.pre_order(bst.r, [])} displayed in new text file")
        elif option == "7":
            if bst is not None:
                with open("books.post_order.txt", "w") as f:
                    old_std_out = sys.stdout
                    sys.stdout = f
                    print("Post Order Traversal")
                    print(bst.post_order(bst.r, []))
                    sys.stdout = old_std_out
                print(f"{bst.post_order(bst.r, [])} displayed in new text file")
        elif option == "8":
            if bst is not None:
                with open("books.bf_traverse.txt", "w") as f:
                    old_std_out = sys.stdout
                    sys.stdout = f
                    print("Breath First Traversal")
                    print(bst.bf_traverse())
                    sys.stdout = old_std_out
                print(f"{bst.bf_traverse()} displayed in new text file")


#main: Create the main menu
def main():
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        3 Test Palindrome
        4 Traversals
        0 Exit/Quit
        """)
        option=input() 
        
        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            menu_test_palindrome()
        elif option == "4":
            menu_traversals()


if __name__ == "__main__":
    main()
