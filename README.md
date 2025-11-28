# 💻 Técnica de Desenvolvimento de Algoritmos - Prova A1

Repositório dedicado a exercícios básicos em Python, desenvolvidos para a avaliação regimental (A1) da disciplina **Técnica de Desenvolvimento de Algoritmos** da UDF.

---

## 📂 Organização do Repositório

O diretório `exercicios/` contém todos os programas desenvolvidos para a avaliação.

exercicios/
├── exercicio1-verificacao-idade.py
├── exercicio2-contar-pares.py
├── exercicio3-lista-alunos.py
└── exercicio4-cadastro-produtos.py

---

## ✨ Detalhamento dos Exercícios

Cada arquivo Python implementa uma funcionalidade específica, conforme descrito abaixo:

---

### 1. `exercicio1-verificacao-idade.py`
**Tema:** Estrutura Condicional Simples.

**Descrição:**  
O programa solicita a idade do usuário e verifica se ela é maior ou igual à maioridade legal (≥ 18). Caso seja, a entrada ao evento é permitida; caso contrário, é negada.
## Fluxograma

mermaid
    flowchart TD
        A([Início]) --> B[Digite sua idade]
        B --> C{idade >= 18?}
        C -->|Sim| D[Entrada permitida]
        C -->|Não| E[Entrada não permitida]
        D --> F([Fim])
        E --> F([Fim])

---

### 2. `exercicio2-contar-pares.py`
**Tema:** Estrutura de Repetição.

**Descrição:**  
Realiza uma contagem de 0 a 100, exibindo somente os números pares. Números ímpares são ignorados durante a iteração.

---

### 3. `exercicio3-lista-alunos.py`
**Tema:** Manipulação de Listas (CRUD Básico) e Menu de Opções.

**Descrição:**  
Sistema com menu interativo para gerenciamento de uma lista de alunos. Funções disponíveis:

- Consultar lista de alunos  
- Adicionar novos alunos  
- Remover alunos existentes  
- Encerrar o programa

---

### 4. `exercicio4-cadastro-produtos.py`
**Tema:** Manipulação de Dicionários (CRUD Básico) e Menu de Opções.

**Descrição:**  
Sistema com menu interativo para gerenciamento de um dicionário de produtos, onde:

- **Chave:** nome do produto  
- **Valor:** preço do produto  

Operações disponíveis:

- Adicionar um novo produto  
- Remover um produto pelo nome  
- Consultar produtos e preços cadastrados  
- Encerrar o programa

---
