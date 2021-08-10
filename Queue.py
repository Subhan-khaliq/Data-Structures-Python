class Queue:
    def __init__(self,size):
        self.size = size
        self.list = list(range(0,self.size))
        self._rear = 0
        self._front = 0
        self._length=0
    def is_full(self):
        if self._length==self.size:
            return True
        else:
            return False
    def is_empty(self):
        if self._length==0:
            return True
        return False
    def index_incrementor(self, index):
        if index + 1 == self.size:
            return 0
        else:
            return index + 1
        
    def enqueue(self, value):
        if self.is_full()==True:
            raise IndexError("No more space in the queue")
        else:
            self.list[self._rear] = value
            self._length=self._length+1
            self._rear = self.index_incrementor(self._rear)
        
        
    def dequeue(self):
        if self.is_empty()==True:
            raise IndexError("Nothing in the queue")
            
        output_value = self.list[self._front]
        self.list[self._front] = 0
        self._length=self._length-1
        self._front = self.index_incrementor(self._front)
        
        return output_value
    
    


q = Queue(3)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())