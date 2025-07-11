class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class stack:
	def __init__(self):
		self.top = None

	def push(self, data):
        # Adiciona um novo nó no topo da pilha
		new_node = Node(data)
		if self.top:
			new_node.next = self.top
		self.top = new_node

	def pop(self):
     # Remove o nó do topo da pilha e retorna seu valor
		if self.top is None:
			return None
		else:
			popped_node = self.top
			self.top = self.top.next
			popped_node.next = None
			return popped_node.data

	def peek(self):
		# Retorna o valor do topo da pilha sem removê-lo
		if self.top:
			return self.top.data
		else:
			return None

	def is_empty(self):
		# Verifica se a pilha está vazia
		return self.top is None

	def unstack(self):
		# Desempilha todos os elementos da pilha
		while not self.is_empty():
			self.pop()
# Exemplo de uso da pilha
stack_books = stack()
stack_books.push("Game of Thrones")
stack_books.push("Harry Potter")
stack_books.push("The Hobbit")
while stack_books.peek(): # Enquanto houver livros na pilha
	print(stack_books.pop())    # Remove e exibe o livro no topo da pilha
