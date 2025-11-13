# Exercício 2: Comparação de Representações de Grafos
O material de referência descreve duas formas de representar um grafo: a Lista de Adjacência e a Lista de Incidência.
Compare as duas, explicando o foco de cada uma (relações vértice-vértice vs. relações vértice-aresta).

# Resposta:
De acordo com o material, as duas formas de representar um grafo têm focos distintos e complementares, como explicitamente comparado no conteúdo:

---

## **Lista de Adjacência: Foco em Relações Vértice-Vértice**

A representação por **lista de adjacência** mostra **quais vértices são vizinhos de quais vértices**, concentrando-se nas relações diretas entre os nós do grafo.

### **Como funciona (conforme o material):**
- Cada vértice possui uma lista de seus vértices adjacentes (vizinhos)
- Implementada como um dicionário onde: `{'v1': ['v2', 'v3', 'v4'], ...}`
- **Exemplo do material**: `v1: ['v2', 'v3', 'v4']` indica que v1 está conectado diretamente a v2, v3 e v4

### **Foco:**
- Responde à pergunta: **"Dado um vértice, quem estão conectados a ele?"**
- É **eficiente em termos de espaço para grafos esparsos** (poucas arestas)
- **Ideal para operações de travessia** (BFS/DFS), pois acessa rapidamente os vizinhos de um vértice

---

## **Lista de Incidência: Foco em Relações Vértice-Aresta**

A representação por **lista de incidência** mostra **quais arestas estão conectadas a quais vértices**, concentrando-se nas conexões entre nós e as arestas que os ligam.

### **Como funciona (conforme o material):**
- Cada vértice possui uma lista das arestas que nele incidem
- Implementada com **duas estruturas** (dentro da classe `Grafo`):
  - `self.vertices`: guarda a lista de incidência → `{'v1': ['e1', 'e2', 'e3'], ...}`
  - `self.arestas`: guarda os detalhes de cada aresta → `{'e1': ('v1', 'v2'), ...}`
- **Exemplo do material**: `v1: ['e1', 'e2', 'e3']` indica que as arestas e1, e2 e e3 estão conectadas ao vértice v1

### **Foco:**
- Responde à pergunta: **"Dado um vértice, quais arestas passam por ele?"**
- **Essencial quando as arestas têm identidade própria** (nomes, pesos, múltiplas conexões)
- **Permite modelar situações reais** como redes de metrô, onde cada linha (aresta) tem significado específico e pode conectar as mesmas estações em horários diferentes

---

## **Comparação Direta (segundo o material)**

| Característica | **Lista de Adjacência** | **Lista de Incidência** |
|----------------|------------------------|------------------------|
| **Foco** | Relação vértice-vértice | Relação vértice-aresta |
| **Estrutura** | `vértice → [lista de vizinhos]` | `vértice → [lista de arestas incidentes]` |
| **Quando usar** | Para **travessia e conectividade** (BFS/DFS) | Para **modelagem detalhada** onde arestas têm identidade |
| **Exemplo do material** | `v1: [v2, v3, v4]` | `v1: [e1, e2, e3]` |
| **Vantagem** | Eficiente para encontrar vizinhos | Captura propriedades específicas de cada aresta |

### **Ilustração do Material:**

**Lista de Adjacência:**
```
v1 → [v2, v3, v4]  # v1 é vizinho de v2, v3 e v4
```

**Lista de Incidência:**
```
v1 → [e1, e2, e3]  # as arestas e1, e2, e3 incidem em v1
e1: (v1, v2)       # detalhes da aresta e1
```

---

## **Conclusão**

Como enfatizado no material, a escolha entre as representações depende do que se deseja priorizar: se a **conectividade entre vértices** (lista de adjacência) ou a **identidade e propriedades das arestas** (lista de incidência). A lista de adjacência responde "quem conhece quem", enquanto a lista de incidência responde "por qual conexão cada um está ligado".