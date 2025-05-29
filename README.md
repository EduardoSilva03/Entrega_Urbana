## Pré-requisitos

* Python 3.x

Não são necessárias bibliotecas externas além das que vêm com a instalação padrão do Python.

## Como Executar

1.  **Clone o repositório** (ou baixe os arquivos) para o seu computador.
2.  **Navegue até a pasta raiz do projeto** (a pasta `entrega_urbana`) pelo seu terminal ou prompt de comando.
    ```bash
    cd caminho/para/entrega_urbana
    ```
3.  **Execute o script principal:**
    ```bash
    python script.py
    ```

## O Que Esperar

Ao executar `script.py`, o programa irá:
* Configurar diferentes cenários de simulação (com/sem obstáculos, com/sem tráfego).
* Rodar algoritmos de busca (A* com heurísticas Manhattan e Euclidiana, e BFS/Dijkstra) para encontrar caminhos no mapa 4x4.
* Imprimir no console os resultados de cada simulação, incluindo:
    * Uma visualização do mapa com o caminho encontrado (se houver).
    * Métricas como custo do caminho, número de passos, nós expandidos pelo algoritmo e tempo de execução.
* Ao final, será exibido um resumo comparativo dos resultados de todas as simulações.

Não há interface gráfica; toda a saída é em formato de texto no console.
