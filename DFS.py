class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()
    def DFS(self,root,key):
        count=0
        l=[]
        l.append(root)
        while l:
            current=l.pop()
            count=count+1
            if key==current.value:
                print(count)
                return current.value
            if current.leftChild:
                l.append(current.leftChild)
            if current.rightChild:
                l.append(current.rightChild)
    
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()
    def DFS(self,key):
        return self.root.DFS(self.root,key)

t1= Tree()
t1.insert(50)
t1.insert(30)
t1.insert(70)
t1.insert(62)
t1.insert(87)
t1.insert(15)
t1.insert(35)
t1.insert(7)
t1.insert(22)
t1.insert(32)
t1.insert(37)
t1.insert(60)
t1.insert(65)
t1.insert(85)
t1.insert(90)
print(t1.DFS(90))