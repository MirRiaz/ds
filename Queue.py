from doublelinkedlist import *

class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self, val):
        self.__list.add(val)

    def dequeue(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def front_element(self):
        return self.__list.front()

    def last_element(self):
        return self.__list.back()

    def is_empty(self):
        if self.__list == 0:
            return "List Is empty"


    def __len__(self):
        return self.__list.size

# my_queue = Queue()
#
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.enqueue(4)
# my_queue.enqueue(10)
#
#
# print(len(my_queue))
#
# print(my_queue.front_element())
#
# print('remove value',my_queue.dequeue())
# print('remove value',my_queue.dequeue())
#
# print('This Element is last',my_queue.last_element())