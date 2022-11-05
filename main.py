from claseGrafoSecuencial import GrafoSecuencial

if __name__ == '__main__':
    #códigos por vértice: A = 0, B = 1, C = 2, D = 3, E = 4, F = 5.
    obj = GrafoSecuencial(6)
    obj.CrearArco(0, 1)
    obj.CrearArco(0, 3)
    obj.CrearArco(1, 2)
    obj.CrearArco(1, 4)
    obj.CrearArco(1, 5)
    obj.CrearArco(2, 3)
    obj.CrearArco(3, 1)
    obj.CrearArco(4, 3)
    obj.CrearArco(4, 5)
    obj.CrearArco(5, 3)
    obj.CrearArco(5, 0)
    obj.Dijkstra(0, 4)#camino mas corto de A a E