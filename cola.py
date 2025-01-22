class Node:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

class Cola:
  def __init__(self):
    self.primero = None
    self.ultimo = None

  def enqueue(self, dato):
    nodo = Node(dato)
    if self.primero is None:
      self.ultimo = nodo
      self.primero = self.ultimo
    else:
      self.ultimo.siguiente = nodo
      self.ultimo = nodo

  def dequeue(self):
    if self.primero is not None:
      if self.primero.siguiente is None:
        valor = self.primero.dato
        self.primero = self.ultimo
        self.ultimo = None
      else:
        valor = self.primero.dato
        self.primero = self.primero.siguiente
        if self.primero.siguiente is None:
          self.ultimo = None
    else:
      print("Ya no hay datos en la cola")

  def show(self):
    actual = self.primero
    while(actual):
      print(actual.dato)
      actual = actual.siguiente


prueba = Cola()
prueba2 = Cola()
prueba.enqueue(5)
prueba.enqueue(6)
prueba.enqueue(7)
prueba.show()

print("-------------")
prueba.dequeue()
prueba.show()
print("-------------")
prueba.dequeue()
prueba.show()
print("-------------")
prueba.dequeue()
prueba.show()
print("-------------")
prueba.dequeue()
prueba.show()