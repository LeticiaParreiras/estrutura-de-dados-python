class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Métodos
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:  # Verifica se já existe head na lista
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:  # Verifica se já existe head na lista
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def delete_at_start(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
            return True
        return False

    def delete_at_end(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
            return True
        return False

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=",")
            current_node = current_node.next
    def print_inverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.data, end=",")
            current_node = current_node.previous


# Demonstração
lista = DoublyLinkedList()
lista.insert_at_beginning(1)
lista.insert_at_end(9)
lista.insert_at_beginning(7)
lista.insert_at_beginning(4)
lista.insert_at_end(10)
lista.delete_at_start()
lista.delete_at_end()
lista.insert_at_beginning(0)
lista.print()
print("\n")
lista.print_inverse()
