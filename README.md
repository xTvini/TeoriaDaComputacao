# TeoriaDaComputacao: Benchmark e Análise do Merge Sort

## Visão Geral
Este projeto fornece um benchmark abrangente e reproduzível e análise do algoritmo Merge Sort implementado tanto em Python quanto em C. Foi projetado para fins educacionais e de pesquisa, permitindo comparar o desempenho, complexidade teórica e eficiência prática do Merge Sort em duas linguagens de programação populares.

## Funcionalidades
- **Duas Implementações:** Merge Sort em Python (`project/mergesort.py`) e C (`project/mergesort.c`).
- **Benchmark Automatizado:** Executa ambas as implementações nos mesmos tamanhos de entrada, múltiplas vezes, coletando média e desvio padrão para cada métrica.
- **Coleta de Dados:** Resultados são salvos como arquivos CSV para ambas as linguagens, incluindo tempo de execução, contagem de recursões e contagem de comparações.
- **Análise Visual:** Gera gráficos claros e prontos para publicação comparando:
  - Tempos de execução medidos
  - Complexidade teórica (O(n log n)) vs. tempos medidos
  - Velocidade de execução (itens/ms) para cada linguagem
  - Todos os gráficos incluem bandas de desvio padrão para clareza estatística
- **Orquestração:** Um único script orquestrador (`project/orchestrator.py`) automatiza todo o processo: limpeza, execução de benchmarks e geração de todas as saídas.
- **Reprodutibilidade:** Todas as etapas, desde a geração de dados até a visualização, são totalmente automatizadas e reproduzíveis.

## Estrutura do Projeto
```
project/
  mergesort.py            # Implementação em Python
  mergesort.c             # Implementação em C
  orchestrator.py         # Orquestra todos os benchmarks e análises
  constants/              # Constantes centralizadas para scripts
  data/                   # Tamanhos de entrada e todos os resultados CSV
  img/                    # Todos os gráficos gerados (PNG)
  ...
requirements.md           # Requisitos do projeto e diretrizes do relatório
```

## Dados de Entrada
A entrada para o processo de benchmarking é controlada pelo arquivo `project/input_sizes.txt`. Este arquivo contém uma lista de inteiros, cada um representando um tamanho específico de array a ser usado para ordenação.

Ambos os scripts de benchmarking Python (`project/mergesort.py`) e C (`project/mergesort.c`) leem esses tamanhos. Para cada tamanho, eles geram dinamicamente arrays preenchidos com inteiros aleatórios. Isso garante que ambas as implementações sejam testadas sob condições idênticas para as dimensões dos arrays.

## Detalhes do Fluxo de Trabalho

O projeto segue um fluxo de trabalho automatizado orquestrado por `project/orchestrator.py`.

### 1. Scripts de Benchmarking
   - **Benchmark Python (`project/mergesort.py`)**:
     - Lê tamanhos de array de `project/input_sizes.txt`.
     - Para cada tamanho, gera arrays de inteiros aleatórios.
     - Executa o algoritmo Merge Sort, medindo tempo de execução, contando recursões e comparações ao longo de múltiplas repetições (definidas em `project/constants/mergesort_constants.py`).
     - Salva os resultados médios e desvios padrão em `project/data/datasheet_python.csv`.
   - **Benchmark C (`project/mergesort.c`)**:
     - Similar ao script Python, lê tamanhos de `project/input_sizes.txt`.
     - Gera arrays aleatórios para cada tamanho.
     - Executa Merge Sort, coletando métricas para tempo, recursões e comparações ao longo de múltiplas repetições.
     - Salva os resultados médios e desvios padrão em `project/data/datasheet_clang.csv`.

### 2. Análise e Visualização (`project/mergesort_comparison.py`)
  - Lê os dados brutos de benchmark de `project/data/datasheet_python.csv` e `project/data/datasheet_clang.csv`.
  - Calcula a complexidade teórica (O(n log n)) baseada nos tamanhos de entrada.
  - Computa velocidade de execução (itens por milissegundo) para ambas as implementações Python e C.
  - Gera gráficos comparativos para:
    - Tempos de execução medidos.
    - Razão do tempo medido para a complexidade teórica.
    - Velocidade de execução.
  - Salva esses gráficos como imagens PNG no diretório `project/img/` (com subdiretórios específicos por linguagem `project/img/python/` e `project/img/clang/`).
  - Cria um arquivo CSV resumo (`project/data/mergesort_comparison_summary.csv`) combinando métricas-chave de ambas as linguagens.

### 3. Orquestração (`project/orchestrator.py`)
  - Este script automatiza todo o pipeline:
    1. **Limpeza (Opcional)**: Se executado com o argumento `--clean`, remove arquivos CSV gerados anteriormente de `project/data/` e imagens de `project/img/`.
    2. **Executar Benchmark Python**: Executa `project/mergesort.py`.
    3. **Compilar e Executar Benchmark C**: Compila `project/mergesort.c` (usando GCC) e então executa o executável compilado.
    4. **Executar Script de Análise**: Executa `project/mergesort_comparison.py` para gerar gráficos e o CSV resumo.

## Como Executar
1.  **Pré-requisitos:**
    *   **Python 3.8 ou mais recente** - Para executar os scripts de benchmarking e análise
    *   **GCC (GNU Compiler Collection)** - Para compilar o código C. Certifique-se de que está no PATH do seu sistema
    *   **Python pip** - Para instalar dependências Python

2.  **Dependências Python:**
    O projeto requer as seguintes bibliotecas Python (listadas em `requirements.txt`):
    *   **pandas** (>=1.5.0) - Para manipulação e análise de dados CSV
    *   **matplotlib** (>=3.6.0) - Para criação de gráficos e visualizações
    *   **seaborn** (>=0.12.0) - Para visualizações estatísticas avançadas
    *   **numpy** (>=1.24.0) - Para computação científica (dependência implícita das outras bibliotecas)

3.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/xTvini/TeoriaDaComputacao.git
    cd TeoriaDaComputacao
    ```

4.  **Criar e Ativar um Ambiente Virtual (Recomendado):**
    É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto:
    
    **No Linux/macOS:**
    ```bash
    # Criar o ambiente virtual
    python3 -m venv venv
    
    # Ativar o ambiente virtual
    source venv/bin/activate
    ```
    
    **No Windows:**
    ```bash
    # Criar o ambiente virtual
    python -m venv venv
    
    # Ativar o ambiente virtual
    venv\Scripts\activate
    ```
    
    Para desativar o ambiente virtual quando terminar:
    ```bash
    deactivate
    ```

5.  **Instalar Dependências Python:**
    Com o ambiente virtual ativado, navegue até o diretório raiz do projeto (onde `requirements.txt` está localizado) e execute:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Executar o Orquestrador:**
    Para executar todo o pipeline de benchmark e análise, execute o script orquestrador do diretório raiz:
    ```bash
    python -m project.orchestrator
    ```
    Se você quiser limpar quaisquer resultados anteriores (CSVs e imagens) antes de executar os benchmarks:
    ```bash
    python -m project.orchestrator --clean
    ```

7.  **Saídas:**
    Após execução bem-sucedida, você encontrará:
    *   Dados brutos de benchmark para Python: `project/data/datasheet_python.csv`
    *   Dados brutos de benchmark para C: `project/data/datasheet_clang.csv`
    *   Dados resumo combinados: `project/data/mergesort_comparison_summary.csv`
    *   Gráficos gerados: no diretório `project/img/` e seus subdiretórios.

Para mais detalhes sobre constantes específicas usadas (como número de repetições, caminhos de arquivo), consulte os arquivos dentro do diretório `project/constants/`. O arquivo `requirements.md` pode conter diretrizes adicionais do projeto ou informações do relatório.

## Solução de Problemas

### Problemas Comuns de Dependências
- **Erro de importação do pandas/matplotlib/seaborn**: 
  - Certifique-se de ter ativado o ambiente virtual com `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
  - Execute `pip install -r requirements.txt` com o ambiente virtual ativado
- **Versão Python incompatível**: Verifique se está usando Python 3.8 ou superior com `python --version`
- **Conflitos de dependências**: Use um ambiente virtual para evitar conflitos com outras instalações Python
- **GCC não encontrado**: Instale o GCC através do gerenciador de pacotes do seu sistema:
  - Ubuntu/Debian: `sudo apt-get install build-essential`
  - macOS: `xcode-select --install`
  - Windows: Instale MinGW ou use WSL

### Problemas de Execução
- **Arquivos de entrada não encontrados**: Certifique-se de executar os comandos do diretório raiz do projeto
- **Falha na compilação C**: Verifique se o GCC está instalado e acessível no PATH
- **Erros de permissão**: Garanta que tem permissões de escrita nos diretórios `project/data/` e `project/img/`