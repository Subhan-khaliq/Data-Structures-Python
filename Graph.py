class Graph:
    def __init__(self):
        self.gr={}
    def add_node(self,node):
        if node in self.gr:
            return 0
        self.gr[node]=[]
    def print(self):
        for i in self.gr:
            print(i)
    def add_edges(self,a,b):
        if a not in self.gr:
            raise Exception("Source not Exist")
        if b not in self.gr:
            raise Exception("Destination not Exist")
        
        edges=self.gr[a]
        
        if b not in edges:
            edges.append(b)
        else:
            raise ValueError("Destination not exist")
        #check if a exists otherwise bhagg jao
        #check if b exists otherwise bhagg jao
        #Add edge i.e. add Node (b) into the list of node(a)