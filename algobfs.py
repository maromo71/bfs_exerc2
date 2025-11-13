def bfs_classico(grafo):
    visitados = set()
    fila = []

    for v in grafo:
        if v not in visitados:
            fila.append(v)
            visitados.add(v)

            while fila:
                v = fila.pop(0)
                print(v, end=' ')
                for vizinho in grafo[v]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)



grafo = {
    "A": ["B", "E", "F"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C", "G"],
    "E": ["A"],
    "F": ["A","G"],
    "G": ["D", "F"]
}

bfs_classico(grafo)
