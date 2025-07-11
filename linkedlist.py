class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
  
	def insert_at_beginning(self, data):
		new_node = Node(data)
		if self.head:  # Check if the list already has a head
			new_node.next = self.head
			self.head = new_node
		else:
			self.tail = new_node
			self.head = new_node
   
	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head:  # Se já há um head, adiciona ao final
			self.tail.next = new_node
			self.tail = new_node
		else:  # Lista vazia, define o novo nó como head e tail
			self.head = new_node
			self.tail = new_node

	def search(self, data):
		current_node = self.head
		while current_node:
			if current_node.data == data:
				return True
			else:
				current_node = current_node.next
		return False

	def print(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next
        
        

lista = LinkedList()
lista.insert_at_beginning(1) # 1
lista.insert_at_beginning(2) # 2 1
lista.insert_at_end(4) # 2 1 4
lista.print()
print(lista.search(3))
print(lista.search(4))
