import queue

# Cria uma fila LIFO
stack_queue = queue.LifoQueue(maxsize = 0) # tamanho 0 = infinito

# Adiciona itens na fila
stack_queue.put(1)
stack_queue.put(2)
stack_queue.put(3)

# Tamanho
print("Tamanho:", stack_queue.qsize())

# Remove e imprime os itens na ordem LIFO
print(stack_queue.get())  # Saída: 3
print(stack_queue.get())  # Saída: 2
print(stack_queue.get())  # Saída: 1


# Esta vazio:
print("Está vazio?", stack_queue.empty())  