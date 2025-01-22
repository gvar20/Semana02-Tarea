class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def Insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def Mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente


    def ELiminar(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.valor == valor:
            self.cabeza == self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.valor == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente



lista = ListaEnlazada()

lista.Insertar(5)
lista.Insertar(3)
lista.Insertar(8)

lista.Mostrar()
print("Eliminar 3")
lista.ELiminar(3)
lista.Mostrar()