class Node:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

class Pila:
  def __init__(self):
    self.ultimo = None

  def push(self, dato):
    nodo = Node(dato)
    if self.ultimo is not None:
      nodo.siguiente = self.ultimo
    self.ultimo = nodo

  def pop(self):
    if self.ultimo is not None:
      ultimo = self.ultimo.dato
      self.ultimo = self.ultimo.siguiente
      return ultimo
    print("Ya no hay elementos en la pila")
    return None

  def show(self):
    actual = self.ultimo
    while(actual):
      print(actual.dato)
      actual = actual.siguiente

pila = Pila()

pila.push(5)
pila.push(15)
pila.push(3)

pila.show()
print("-----------")
pila.pop()
pila.show()
print("-----------")
pila.pop()
pila.show()
print("-----------")
pila.pop()
pila.show()
print("-----------")
pila.pop()
pila.show()