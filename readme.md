# Instruções para Início

Siga estes passos para construir seu roteirizador.

---

## **Passo 1: Representar o Grafo**

Primeiro, crie em seu script Python a estrutura de dados que representa o grafo acima. A melhor forma de fazer isso é usando um dicionário (para a Lista de Adjacência).

### Dica: Estrutura da sua Lista de Adjacência
```python
grafo_cidades = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': []  # Cidade 'G' está isolada
}
```

---

## **Passo 2: A Função `encontrar_caminho_bfs`**

Crie uma função que receba o grafo, a cidade de origem e a cidade de destino.
```python
def encontrar_caminho_bfs(grafo, origem, destino):
    # ... seu código aqui ...
```

---

## **Passo 3: Adaptar o BFS (O Ponto-Chave)**

O algoritmo BFS que vimos em aula é excelente para saber se um nó é alcançável. Para saber o caminho até ele, precisamos de uma pequena adaptação: precisamos "lembrar" de onde viemos.

Para isso, além da fila (para o BFS) e do conjunto visitados, você deve usar uma estrutura (idealmente um dicionário) que chamaremos de **parentes**.

### Lógica
Quando você está em uma `cidade_atual` e descobre um vizinho que ainda não foi visitado, você deve:

1. Adicioná-lo à fila para explorá-lo depois.
2. Marcá-lo como visitado.
3. Registrar: `parentes[vizinho] = cidade_atual` (Isso salva a informação: "Eu cheguei em vizinho vindo de cidade_atual").

---

## **Passo 4: Rastrear o Caminho de Volta**

O seu loop BFS termina quando a fila fica vazia (ou quando você encontra o destino). Após o loop, verifique:

1. O destino foi encontrado? (Verifique se destino está no seu conjunto visitados ou no seu dicionário parentes).
2. Se **NÃO** foi encontrado (ex: buscando um caminho para 'G'): Retorne uma mensagem clara, como `"Não há caminho entre {origem} e {destino}."`.
3. Se **FOI** encontrado: Agora, use o dicionário parentes para reconstruir o caminho.
   - Comece uma lista `caminho = [destino]`.
   - Faça um loop (while): pegue o último item do caminho (ex: `cidade_atual = destino`) e adicione o "pai" dele (`parentes[cidade_atual]`) ao início da lista.
   - Continue fazendo isso até que o "pai" seja a origem.
   - (Não se esqueça de adicionar a origem no final e reverter a lista, ou construir a lista de trás para frente).
   - Retorne a lista caminho final.

---

## **Passo 5: Testes Obrigatórios**

Ao final do seu script, inclua os seguintes testes para validar sua função (`main.py`):

### Teste 1: Caminho existente
```python
caminho_1 = encontrar_caminho_bfs(grafo_cidades, 'A', 'F')
print(f"Caminho de A para F: {caminho_1}")
# Saída esperada (BFS encontra o caminho mais curto em "saltos"):
# Caminho de A para F: ['A', 'C', 'F']
```

### Teste 2: Caminho mais longo
```python
caminho_2 = encontrar_caminho_bfs(grafo_cidades, 'D', 'F')
print(f"Caminho de D para F: {caminho_2}")
# Saída esperada:
# Caminho de D para F: ['D', 'B', 'E', 'F'] ou ['D', 'B', 'A', 'C', 'F']
# (Note: BFS garante ['D', 'B', 'E', 'F'] pois tem 3 saltos vs 4)
```

### Teste 3: Cidade isolada
```python
caminho_3 = encontrar_caminho_bfs(grafo_cidades, 'A', 'G')
print(f"Caminho de A para G: {caminho_3}")
# Saída esperada:
# Caminho de A para G: Não há caminho entre A e G.
```

### Teste 4: Origem e Destino iguais
```python
caminho_4 = encontrar_caminho_bfs(grafo_cidades, 'C', 'C')
print(f"Caminho de C para C: {caminho_4}")
# Saída esperada:
# Caminho de C para C: ['C']
```