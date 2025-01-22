class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def Insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._InsertarRecursivo(self.raiz, valor)
    
    def _InsertarRecursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._InsertarRecursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._InsertarRecursivo(nodo.derecho, valor)

    def Mostrar(self):
        self._MostrarRecursivo(self.raiz)

    def _MostrarRecursivo(self, nodo):
        if nodo is not None:
            self._MostrarRecursivo(nodo.izquierdo)
            print(nodo.valor)
            self._MostrarRecursivo(nodo.derecho)


arbol = ArbolBinario()
arbol.Insertar(15)
arbol.Insertar(20)
arbol.Insertar(5)
arbol.Insertar(16)

arbol.Mostrar()