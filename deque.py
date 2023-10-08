
from collections import deque

my_queue = Queue()
my_queue.enqueue(1)
print(len(my_queue))
print(my_queue.front())
my_queue.enqueue(1)
my_queue.enqueue(4)
my_queue.enqueue(10)
my_queue.enqueue(111)
print(my_queue.front())
print(len(my_queue))
print(my_queue.deque())
print(my_queue.front())
my_queue.deque()
print(my_queue.front())