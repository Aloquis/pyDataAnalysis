# Implementação do Mínimos Quadrados Recursivos (MQR)

Este projeto é parte do meu repositório em **pyDataAnalysis**. O objetivo é implementar o algoritmo de Mínimos Quadrados Recursivos (MQR ou RLS - *Recursive Least Squares*) em Python para estimar os parâmetros de um sistema dinâmico.

---

## Descrição

O algoritmo de **Mínimos Quadrados Recursivos (MQR)** é um método adaptativo usado para identificar os parâmetros de um sistema em tempo real. Diferente do método de mínimos quadrados em lote, o MQR atualiza as estimativas dos parâmetros a cada nova amostra de dados que recebe.

**Objetivo deste código:** São três códigos: minimosQuadradosRecursivos.py, leitorCsv.py e gerarDadosPrecal.py. Esses três códigos se inteiram numa simulação/protótipo de como funcionaria o MQR.

---

## Como Usar

Siga os passos abaixo para executar o projeto no seu ambiente local.

### Pré-requisitos

* Python 3.8 ou superior
* Um ambiente Linux (como Ubuntu/WSL) ou macOS

### Passos para Execução

1.  **Clone o repositório (se ainda não o fez):**
    ```bash
    git clone https://github.com/Aloquis/pyDataAnalysis.git
    cd pyDataAnalysis/projetoMinimoQuadradoRecursivo
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script:**
    ```bash
    python3 minimosQuadradosRecursivos.py
    ```

---

## Estrutura do Projeto

```
projetoMinimoQuadradoRecursivo/
│
├── README.md                
├── requirements.txt         # Lista de dependências Python
├── leitorCSV.py
├── gerarDadosPrecal.py
├── minimosQuadradosRecursivos.py  # Script principal 
└── data/
    └── dadosFinais.csv # Dados de entrada/saída para o sistema
```

---

## Resultados

Após a execução, o script principal gera um gráfico de k+1 predições do algoritmo RLS e outro das reais temperaturas (simuladas) lidas no arquivo dadosFinais.csv.

Os scripts secundários: gerarDadosPrecal.py e leitorCsv.py funcionam, respectivamente, da seguinte forma: gera dados excitantes e de certa forma diferentes a cada run; script para facilitar a leitura desses dados CSV no arquivo principal.

---

## Tecnologias Utilizadas

* **Python 3**
* **NumPy:** Para cálculos numéricos e manipulação de vetores/matrizes.
* **Matplotlib:** Para a visualização dos dados e resultados.
* **Pandas:** Para carregar os dados csv.
