# Exercício 1: 
## Estratégias de Exploração e Estruturas de Dados
Descreva e compare as estratégias de exploração da Busca em Largura (BFS) e da Busca em Profundidade (DFS), conforme descrito no material ('ondas' vs. 'mergulho'). Em seguida, explique qual estrutura de dados (Pilha ou Fila) cada algoritmo utiliza e por que a escolha dessa estrutura (LIFO ou FIFO) é o que, fundamentalmente, define a estratégia de exploração de cada um.


## Busca em Largura (BFS) – Exploração em "Ondas"
O material descreve que a BFS "explora o grafo nível por nível" e "ocorre em 'ondas'". O algoritmo começa em um ``nó``  raiz e primeiro visita todos os seus vizinhos diretos antes de avançar para os vizinhos desses vizinhos. Essa abordagem garante que a distância do ``nó`` inicial aumente gradualmente, como ondas que se expandem a partir de um ponto central. O processo é visualizado no material como uma progressão sistemática onde a fila de nós a serem visitados cresce horizontalmente antes de avançar verticalmente.


## Busca em Profundidade (DFS) – Estratégia de "Mergulho"
Conforme explicitado no material, a DFS  "mergulha o mais fundo possível em um grafo", explorando um único caminho até não poder mais avançar. Só então o algoritmo "retrocede para o último ponto onde havia opções não exploradas" e continua. Essa estratégia prioriza a profundidade sobre a amplitude, seguindo um caminho até seu extremo antes de considerar alternativas. A analogia do material compara isso a "mergulhar" no grafo, priorizando ir sempre para frente até o fim.

## Estruturas de Dados e sua Função Definidora
### BFS utiliza uma FILA (FIFO – First-In, First-Out)
O material afirma categoricamente: "A principal ferramenta do BFS é uma fila (Queue) para gerenciar a ordem de visitação dos nós." A fila segue o princípio FIFO, onde o primeiro elemento a entrar é o primeiro a sair. No contexto da BFS:
* Quando um nó é visitado, todos os seus vizinhos não visitados são enfileirados (adicionados ao final da fila)
* O próximo nó a ser processado é sempre o primeiro da fila (o mais antigo)
* Isso garante que nós descobertos mais cedo (mais próximos do raiz) sejam processados antes que nós descobertos mais tarde (mais distantes)

**Por que a Fila define a estratégia "ondas":** A natureza FIFO força o algoritmo a processar nós na ordem exata de sua descoberta. Como todos os vizinhos de um nível são descobertos antes que qualquer vizinho do próximo nível seja processado, a exploração ocorre naturalmente nível por nível, criando o efeito de "ondas".

### DFS utiliza uma PILHA (LIFO – Last-In, First-Out)
O material é claro: "DFS usa uma pilha (Last In, First Out) para controlar a ordem de visita." A pilha segue o princípio LIFO, onde o último elemento adicionado é o primeiro a ser removido. No funcionamento da DFS:
* Quando um nó é visitado, seus vizinhos não visitados são empilhados (adicionados ao topo da pilha)
* O próximo nó a ser processado é sempre o último que foi empilhado (o mais recente)
* Isso faz o algoritmo seguir sempre pelo caminho mais recentemente descoberto

**Por que a Pilha define a estratégia "mergulho":** A natureza LIFO cria um comportamento de "profundidade" porque o algoritmo sempre prioriza o ``nó`` mais recentemente descoberto. Ao empilhar vizinhos, o último vizinho adicionado será o próximo a ser explorado, fazendo o algoritmo "mergulhar" cada vez mais fundo antes de retornar e explorar alternativas. O material reforça: "Isso faz com que o algoritmo vá o mais fundo possível em um caminho antes de voltar".

## Conclusão
Fundamentalmente, a escolha entre FIFO e LIFO é o que distingue BFS de DFS, como enfatizado no material:
* **FIFO (Fila)** = Exploração em amplitude (ondas) – Primeiros descobertos, primeiros explorados
* **LIFO (Pilha)** = Exploração em profundidade (mergulho) – Últimos descobertos, primeiros explorados