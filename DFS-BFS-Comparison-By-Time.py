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
    def BFS(self,root,key):
        count=0
        list1=[]
        list1=[root]
        while list1:
            current=list1.pop(0)
            if current.value==key:
                print(count)
                return True
            if current.leftChild!=None:
                list1.append(current.leftChild)
            if current.rightChild!=None:
                list1.append(current.rightChild)
            count=count+1
        return False
    def DFS(self,root,key):
        count=0
        list1=[]
        list1=[root]
        while list1:
            current=list1.pop()
            if current.value==key:
                print(count)
                return True
            if current.leftChild!=None:
                list1.append(current.leftChild)
            if current.rightChild!=None:
                list1.append(current.rightChild)
            count=count+1
        print(count)
        return False
class Tree:
    def __init__(self):
        self.root = None
        self.leftChild=None
        self.rightChild=None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
  
    def inorder(self):
        if self.root is not None:
            print("InOrder")
            self.root.inorder()
    def BFS(self,key):
        return self.root.BFS(self.root,key)
    def DFS(self,key):
        return self.root.DFS(self.root,key)
t1=Tree()
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
#t1.inorder()
print(t1.BFS(37))
print(t1.DFS(47))