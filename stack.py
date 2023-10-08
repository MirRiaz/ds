from doublelinkedlist import *


class Stack:
    def __init__(self):
        self.__internal_list = []
        self.__list = DoubleLinkedList()

    def push(self, val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size == 0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size

# my_stack = Stack()
#
# my_stack.push(1)
# my_stack.push(2)   # LIFO(Last in fast out) first number is 1 then 2,3,5,7
#                   # So this model is remove the last number 7 the remove 5 and and serail maintain
# my_stack.push(3)
# my_stack.push(5)
# my_stack.push(7)
# print('Last Number is ',my_stack.peek())
#
# print('This is list size:',len(my_stack))
#
# print('Delete Element:', my_stack.pop())
# print('This is list size:',len(my_stack))
# print('Last Number is ',my_stack.peek())







