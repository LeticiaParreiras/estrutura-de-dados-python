import queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def pre_order(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_node(self.root, value)

    def _insert_node(self, current, value):
        if value < current.value:
            if current.left_child is None:
                current.left_child = Node(value)
            else:
                self._insert_node(current.left_child, value)
        else:
            if current.right_child is None:
                current.right_child = Node(value)
            else:
                self._insert_node(current.right_child, value)
                
    def findNode(self, value):
        if self.root == None:
            return False
        current_node = self.root
        while current_node:
            if value < current_node.value and current_node.left_child:
                current_node = current_node.left_child
            elif value > current_node.value and current_node.right_child:
                current_node = current_node.right_child
            else:    
                return current_node.value == value
    def findMin(self):
        if self.root == None:
            return False
        current_node = self.root
        while current_node:
            if current_node.left_child:
                current_node = current_node.left_child
            else:
                return current_node.value
    def findMax(self):
        if self.root == None:
            return False
        current_node = self.root
        while current_node:
            if current_node.right_child:
                current_node = current_node.right_child
            else:
                return current_node.value
                
    # Busca em Profundidade Pre Ordem
    def pre_order(self):
        if self.root:
            self.root.pre_order()
    # Busca em largura / Breadth-First Search
    def bfs(self):
        if self.root == None:
            return False
        else:
            line = queue.Queue(maxsize=0)
            line.put(self.root)
        
            while not line.empty():
                current_node = line.get()
                print(current_node.value)
        
                if current_node.left_child:
                    line.put(current_node.left_child)
        
                if current_node.right_child:
                    line.put(current_node.right_child)
                    
                
arvore = BinaryTree()
arvore.insert(5)
arvore.insert(2)
arvore.insert(1)
arvore.insert(3)
arvore.insert(4)
arvore.insert(7)
arvore.insert(6)
arvore.insert(8)
print(arvore.findNode(5))
print(arvore.findNode(9))
print(f"Menor valor:{arvore.findMin()}")
print(f"Maior valor:{arvore.findMax()}")
