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

    def locateNode(self, value):
        if self.left_child and self.left_child.value == value:
            return self, self.left_child
        elif self.right_child and self.right_child.value == value:
            return self, self.right_child
        elif value < self.value and self.left_child:
            return self.left_child.locateNode(value)
        elif value > self.value and self.right_child:
            return self.right_child.locateNode(value)
        return None, None

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current.value

    def deleteNode(self, value):
        parent, node = self.locateNode(value)
        if node is None:
            return False
    
        # Caso 1: Nó folha
        if node.left_child is None and node.right_child is None:
            if parent.left_child == node:
                parent.left_child = None
            else:
                parent.right_child = None
    
        # Caso 2: Só filho à esquerda
        elif node.left_child and node.right_child is None:
            if parent.left_child == node:
                parent.left_child = node.left_child
            else:
                parent.right_child = node.left_child
    
        # Caso 3: Só filho à direita
        elif node.right_child and node.left_child is None:
            if parent.left_child == node:
                parent.left_child = node.right_child
            else:
                parent.right_child = node.right_child
    
        # Caso 4: Dois filhos
        else:
            successor_value = node.find_minimum_value()
            node.value = successor_value
            node.deleteNode(successor_value)
    
        return True



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
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left_child
            else:
                current = current.right_child
        return False

    def deleteNode(self, value):
        if self.root is None:
            return False
        if self.root.value == value:
            # Casos especiais para remover raiz
            pseudo_root = Node(0)
            pseudo_root.left_child = self.root
            result = self.root.deleteNode(value)
            self.root = pseudo_root.left_child
            return result
        return self.root.deleteNode(value)

    def findMin(self):
        if self.root is None:
            return None
        current = self.root
        while current.left_child:
            current = current.left_child
        return current.value

    def findMax(self):
        if self.root is None:
            return None
        current = self.root
        while current.right_child:
            current = current.right_child
        return current.value

    def pre_order(self):
        if self.root:
            self.root.pre_order()

    def bfs(self):
        if self.root is None:
            return
        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()
            print(current.value)

            if current.left_child:
                q.put(current.left_child)
            if current.right_child:
                q.put(current.right_child)


# 🌳 Execução de teste
if __name__ == "__main__":
    arvore = BinaryTree()
    for val in [5, 2, 1, 3, 4, 7, 6, 8]:
        arvore.insert(val)

    print("Existe o valor 4?", arvore.findNode(4))
    print("Pré-ordem antes de remover 4:")
    arvore.pre_order()

    arvore.deleteNode(4)
    print("\nExiste o valor 4 após remoção?", arvore.findNode(4))
    print("Pré-ordem após remover 4:")
    arvore.pre_order()

    print(f"\nMenor valor: {arvore.findMin()}")
    print(f"Maior valor: {arvore.findMax()}")
