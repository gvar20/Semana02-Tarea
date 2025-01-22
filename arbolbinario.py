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

    def ELiminar(self, valor):
        self.raiz = self._EliminarRecursivo(self.raiz, valor)
        if self.raiz == None:
            print("El arbol esta vacio")

    def _EliminarRecursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self._EliminarRecursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._EliminarRecursivo(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            nodo.valor = self._EncontrarMinimo(nodo.derecho)
            nodo.derecho = self._EliminarRecursivo(nodo.derecho, nodo.valor)
        return nodo

    def _EncontrarMinimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual.valor

arbol = ArbolBinario()
arbol.Insertar(15)
arbol.Insertar(20)
arbol.Insertar(5)
arbol.Insertar(16)

arbol.Mostrar()
print("ELiminar 20 del arbol")
arbol.ELiminar(20)
arbol.Mostrar


print("Eliminar mostrar arbol vacio")
arbol.ELiminar(15)
arbol.ELiminar(5)
arbol.ELiminar(16)
arbol.Mostrar
