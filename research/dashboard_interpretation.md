# Merge Sort - C Implementation Analysis

## 📊 Gráfico 1 — Tempo Real / (n log n)
**Título:** Measured Time / Theoretical n log n - C  
**Eixo X:** InputSize (tamanho da entrada)  
**Eixo Y:** Tempo dividido por n log n (ms / (n log n))  
**Comportamento:** Ligeiramente decrescente

### 🧠 Interpretação:
Este gráfico compara o tempo real medido com o tempo esperado pela complexidade teórica O(n log n).
- Se a razão é constante → tempo cresce exatamente como n log n
- Se a razão cai → o tempo está crescendo mais devagar do que n log n
- Se a razão sobe → o tempo cresce mais rápido do que n log n

### 📌 O que está acontecendo:
Como está ligeiramente decrescente, isso indica que o tempo de execução cresce um pouco mais devagar que n log n. Pode ser por overhead fixo no código que se dilui com n, ou por melhor uso de cache/memória em entradas maiores.

## 📊 Gráfico 2 — Velocidade (itens/ms)
**Título:** Merge Sort: Execution Speed (items/ms) - C  
**Eixo X:** InputSize  
**Eixo Y:** Velocidade (elementos processados por milissegundo)  
**Comportamento:** Decrescente

### 🧠 Interpretação:
Este gráfico mostra a eficiência bruta: quantos elementos são processados por milissegundo.
- Se a velocidade cai → tempo por item está aumentando → desempenho piora
- Se a velocidade fica estável → tempo por item constante → boa escalabilidade
- Se a velocidade sobe (raro) → tempo por item melhora (pode ser otimizações de hardware ou ruído)

### 📌 O que está acontecendo:
A velocidade está caindo, o que faz sentido para algoritmos O(n log n), porque o tempo por item não é constante — ele cresce com log n. Cada item leva mais tempo quanto maior o n.

## 📊 Gráfico 3 — Tempo Total (ms)
**Título:** Merge Sort: Measured Execution Time (ms) - C  
**Eixo X:** InputSize (escala logarítmica)  
**Eixo Y:** Tempo de execução (ms)  
**Comportamento:** Crescente (reta quase perfeita)

### 🧠 Interpretação:
Este é o gráfico bruto de tempo que o algoritmo levou para rodar.
- Se cresce linearmente em escala log-log → comportamento O(n)
- Se cresce um pouco acima da linha reta → comportamento O(n log n)
- Se curva for mais acentuada → pior (ex: O(n²))

### 📌 O que está acontecendo:
O gráfico está crescendo com regularidade, o que bate com a complexidade O(n log n) do Merge Sort. A forma da curva parece consistente com o esperado para esse algoritmo.
