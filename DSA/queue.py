class Queue:
    def __init__(self):
        self.list1=[]
    def enqueue(self, val):
        if len(self.list1) > 5:
            print("Queue Overflow!")
            return
        self.list1.append(val)
    def dequeue(self):
        if self.list1:
            print("popped element is: ",self.list1.pop(0))
            return
        print("queue underflow")
    def peek(self):
        if self.list1:
            print("peek element is: ",self.list1[0])
            return
        print("Queue is empty!")

obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print(obj.list1)
obj.peek()
obj.dequeue()
obj.dequeue()