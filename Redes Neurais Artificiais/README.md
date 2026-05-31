# Resolução de Sudoku 4x4 com Rede Neural Artificial Multicamadas

## Integrantes

* Beatriz Augusta Coelho Bezerra
* Daniel Ramos Maia

---

# Descrição do Projeto

Este projeto apresenta uma solução baseada em Redes Neurais Artificiais (RNA) Multicamadas para resolver o quebra-cabeça Sudoku 4x4.

O objetivo é treinar uma RNA capaz de reconhecer padrões em tabuleiros incompletos e gerar a solução completa correspondente.

O Sudoku utilizado possui uma grade 4x4 dividida em subgrupos 2x2, preenchidos com números pertencentes ao conjunto:

```text
S = {1, 2, 3, 4}
```

A solução desenvolvida gera automaticamente conjuntos de treinamento e teste, realiza o treinamento da rede neural e produz soluções para novos tabuleiros incompletos.

---

# Regras do Sudoku 4x4

A solução deve respeitar as seguintes restrições:

1. Cada célula contém apenas um número pertencente ao conjunto S.
2. Não pode haver repetição de números em uma mesma linha.
3. Não pode haver repetição de números em uma mesma coluna.
4. Não pode haver repetição de números dentro de cada subgrupo 2x2.
5. Cada linha deve conter exatamente os números 1, 2, 3 e 4.
6. Cada coluna deve conter exatamente os números 1, 2, 3 e 4.

---

# Estrutura do Projeto

```text
sudoku-rna/
│
├── train.csv
├── test.csv
├── sudoku_model.pkl
│
├── src/
│   ├── generator.py
│   ├── dataset.py
│   ├── model.py
│   ├── train.py
│   ├── predict.py
│   └── validator.py
│
├── requirements.txt
└── README.md
```

---

# Funcionamento da Solução

## 1. Geração do Dataset

O arquivo `generator.py` cria automaticamente milhares de exemplos válidos de Sudoku 4x4.

Para cada tabuleiro:

* É gerada uma solução válida.
* Algumas posições são removidas aleatoriamente.
* O tabuleiro incompleto é utilizado como entrada.
* O tabuleiro completo é utilizado como saída desejada.

Exemplo:

### Entrada

```text
1 0 3 4
3 4 0 2
0 1 4 3
4 0 2 1
```

### Saída Esperada

```text
1 2 3 4
3 4 1 2
2 1 4 3
4 3 2 1
```

---

## 2. Preparação dos Dados

O arquivo `dataset.py` realiza:

* Leitura dos arquivos CSV.
* Separação entre entradas e saídas.
* Conversão dos dados para arrays NumPy.

---

## 3. Rede Neural Artificial Multicamadas

A RNA utilizada é um Multi-Layer Perceptron (MLP) implementado com Scikit-Learn.

Arquitetura:

```text
Entrada: 16 neurônios

Camada Oculta 1: 128 neurônios
Camada Oculta 2: 256 neurônios
Camada Oculta 3: 128 neurônios

Saída: 16 neurônios
```

Função de ativação:

```text
ReLU
```

Otimizador:

```text
Adam
```

---

## 4. Treinamento

O treinamento é realizado pelo arquivo `train.py`.

O modelo aprende a mapear:

```text
Sudoku Incompleto
        ↓
Sudoku Completo
```

Após o treinamento, o modelo é salvo em:

```text
sudoku_model.pkl
```

---

## 5. Predição

O arquivo `predict.py`:

1. Gera um Sudoku incompleto.
2. Carrega o modelo treinado.
3. Produz uma solução.
4. Compara com a solução correta.
5. Verifica se a solução gerada é válida.

Exemplo de execução:

```text
TABULEIRO INICIAL

4 3 2 1
2 1 4 0
0 0 1 0
1 2 0 0

SOLUÇÃO GERADA PELA RNA

4 3 2 1
2 1 4 3
3 4 1 2
1 2 3 4

SOLUÇÃO CORRETA

4 3 2 1
2 1 4 3
3 4 1 2
1 2 3 4

Sudoku válido? True
Solução idêntica à correta? True
```

---

## 6. Validação

O arquivo `validator.py` verifica:

### Linhas

Cada linha deve conter:

```text
1 2 3 4
```

sem repetições.

### Colunas

Cada coluna deve conter:

```text
1 2 3 4
```

sem repetições.

### Subgrupos

Cada bloco 2x2 deve conter:

```text
1 2 3 4
```

sem repetições.

---

# Discussão: Raciocínio versus Geração de Amostras

O Sudoku é tradicionalmente classificado como um Problema de Satisfação de Restrições (Constraint Satisfaction Problem - CSP).

Uma abordagem baseada apenas na geração aleatória de amostras e testes sucessivos pode encontrar soluções válidas, porém apresenta custo computacional elevado conforme o tamanho do tabuleiro aumenta.

As Redes Neurais Artificiais não executam raciocínio lógico explícito. Em vez disso, aprendem padrões estatísticos a partir dos exemplos fornecidos durante o treinamento.

Assim, a RNA pode prever soluções semelhantes às observadas anteriormente, mas não garante matematicamente que todas as regras do Sudoku serão respeitadas em todos os casos.

Por esse motivo, sistemas reais frequentemente combinam técnicas de aprendizado de máquina com algoritmos de busca e validação.

---

# Generalização para Sudoku NxN

A principal dificuldade para generalizar a solução consiste no crescimento exponencial do espaço de busca.

Exemplos:

```text
4x4  → 16 células
9x9  → 81 células
16x16 → 256 células
```

À medida que N aumenta:

* Cresce a quantidade de entradas.
* Cresce a quantidade de saídas.
* Cresce o número de restrições.
* Cresce o número de combinações possíveis.

Uma rede treinada para Sudoku 4x4 não consegue resolver automaticamente um Sudoku 9x9 ou 16x16 sem treinamento adicional e alterações arquiteturais.

---

# Tecnologias Utilizadas

* Python 3
* NumPy
* Pandas
* Scikit-Learn
* Joblib

---

# Como Executar

## Instalar dependências

```bash
pip install numpy pandas scikit-learn joblib
```

## Gerar o dataset

```bash
python src/generator.py
```

## Treinar a rede

```bash
python src/train.py
```

## Executar predição

```bash
python src/predict.py
```
