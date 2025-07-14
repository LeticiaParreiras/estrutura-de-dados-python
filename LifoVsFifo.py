import queue

# Cria uma fila LIFO (último a entrar, primeiro a sair - pilha)
stack_queue = queue.LifoQueue(maxsize = 0) # tamanho 0 = infinito

# Cria uma fila FIFO (primeiro a entrar, primeiro a sair - fila)
fifo_queue = queue.Queue(maxsize=0)

# Adiciona itens na fila LIFO
stack_queue.put(1)
stack_queue.put(2)
stack_queue.put(3)

# Adiciona itens na fila na fila FIFO
fifo_queue.put(1)
fifo_queue.put(2)
fifo_queue.put(3)

# Remove e imprime os itens na ordem LIFO
print("Remoção da LIFO:")
print(stack_queue.get())  # Saída: 3
print(stack_queue.get())  # Saída: 2
print(stack_queue.get())  # Saída: 1

# Remove e imprime os itens na ordem FIFO
print("Remoção da FIFO:")
print(fifo_queue.get())  # Saída: 1
print(fifo_queue.get())  # Saída: 2
print(fifo_queue.get())  # Saída: 3
