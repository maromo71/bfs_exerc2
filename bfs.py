from collections import deque
def encontrar_caminho_bfs(grafo, origem, destino):
    # 1. vamos verificar se origem é igual a destino. neste caso 
    # especial finalizaos retornando a lista contendo apenas o nome da
    # cidade
    if origem == destino:
        return [origem]
    
    
    # Estrutura de dados adaptadas passo 3 (para o bfs)
    fila = deque() # iniciamos a fila vazia para o BFS
    visitados = set() # iniciamos o conjunto dos visitados
    parentes = {} # dicionario para rastrear caminhos
    
    
    # iniciamos o processo
    fila.append(origem)
    visitados.add(origem)

    while fila:
        # cidade_atual recebe o primeiro da fila
        cidade_atual = fila.popleft()
        

        # explorando os vizinhos da cidade_atual (passo 3)
        for vizinho in grafo[cidade_atual]:
            if vizinho not in visitados:
                # adicionar o vizinho a fila para futura exploracao
                fila.append(vizinho)
                # adiciona o vizinho ao conjnto de vizitado
                visitados.add(vizinho)
                # registrar o vizinho de onde viemos
                parentes[vizinho] = cidade_atual

            if vizinho == destino:
                # encontramos o destino
                return reconstruir_caminho(parentes, origem, destino)

    # neste ponto, chegando aqui significa que nao possui caminho
    return f"Não há caminho entre {origem} e {destino}."


#Passo 4 - Rastrear o caminho de volta
def reconstruir_caminho(parentes, origem, destino):
    caminho = [destino]
    cidade_atual = destino

    # voltar ate a origem 
    while cidade_atual != origem:
        cidade_atual = parentes[cidade_atual]
        caminho.insert(0, cidade_atual)

    return caminho

