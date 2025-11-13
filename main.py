from bfs import encontrar_caminho_bfs

def main():
    # Dica: Estrutura da sua Lista de Adjacência
    grafo_cidades = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        'G': []  # Cidade 'G' está isolada
    }

    # Teste 1: Caminho existente
    caminho_1 = encontrar_caminho_bfs(grafo_cidades, 'A', 'F')
    print(f"Caminho de A para F: {caminho_1}")
    # Saída esperada (BFS encontra o caminho mais curto em "saltos"):
    # Caminho de A para F: ['A', 'C', 'F']

    # Teste 2: Caminho mais longo
    caminho_2 = encontrar_caminho_bfs(grafo_cidades, 'D', 'F')
    print(f"Caminho de D para F: {caminho_2}")
    # Saída esperada:
    # Caminho de D para F: ['D', 'B', 'E', 'F'] ou ['D', 'B', 'A', 'C', 'F']
    # (Note: BFS garante ['D', 'B', 'E', 'F'] pois tem 3 saltos vs 4)

    # Teste 3: Cidade isolada
    caminho_3 = encontrar_caminho_bfs(grafo_cidades, 'A', 'G')
    print(f"Caminho de A para G: {caminho_3}")
    # Saída esperada:
    # Caminho de A para G: Não há caminho entre A e G.

    # Teste 4: Origem e Destino iguais
    caminho_4 = encontrar_caminho_bfs(grafo_cidades, 'C', 'C')
    print(f"Caminho de C para C: {caminho_4}")
    # Saída esperada:
    # Caminho de C para C: ['C']


if __name__ == "__main__":
    main()

