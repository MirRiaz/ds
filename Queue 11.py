class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.queue is not None:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display()

q.dequeue()
q.display()