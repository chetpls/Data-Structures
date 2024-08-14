import numpy as np
from ArrayStack import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack()
        for char in s:
            if char == '(':
                stack.push(char)
            elif char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    def build_parse_tree(self, exp: str) -> str:
        # todo
        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node('')
        u = t.r
        operators = ["+", "-", "*", "/"]
        if self.dict.size() == 0:
            return t
        for i in exp:
            if i == "(":
                u.insert_left()
                u = u.left
            elif i == ")":
                u = u.parent
            elif i in operators:
                u.x = i
                u.insert_right()
                u = u.right
            else:
                u.x = i
                u = u.parent
        return t

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        left = root.left
        right = root.right
        if left != None and right != None:
            fn = op[root.x]
            return fn(self._evaluate(left), self._evaluate(right))
        elif left is None and right is None:
            t = self.dict.find(root.x)
            if t != None:
                return t
            return root.x
        else:
            if left is not None:
                return self._evaluate(left)
            else:
                return self._evaluate(right)

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        

