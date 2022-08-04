class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def get_queue(self):
        return self.queue

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)


queue = Queue()
queue.enqueue("X")
queue.enqueue("Y")
queue.dequeue()
queue.enqueue("Z")

print(queue.get_queue())
