
class Queue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue==[]

    def enqueue(self,item):
        self.queue.insert(0,item)

    def dequeue(self):
        self.queue.pop()

    def getSize(self):
        return len(self.queue)