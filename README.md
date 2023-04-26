# Repositório do projeto `Algorithms` 🤖

## Módulo: CIÊNCIA DA COMPUTAÇÃO

 Repositório possuí projeto desenvolvido no período que estive na **Trybe**, abordando conceitos de `Complexidade de algoritmos`, `recursividade e estratégias para solução de problemas` e `algoritmos de ordenação e busca`.

## Informações de aprendizados

- Este é um projeto desenvolvido para praticar `Python`;
- Utilizei o `Pytest` para fazer meus testes;

## Linguagens e ferramentas usadas

[![Git][Git-logo]][Git-url]
[![Python][Python-logo]][Python-url]
[![Pytest][Pytest-logo]][Pytest-url]

## O que foi desenvolvido

Neste projeto, resolvi problemas e otimizei algoritmos desenvolvendo a minha capacidade de implementar soluções para os mais diversos problemas do dia a dia!

## Habilidades trabalhadas

- Lógica;
- Capacidade de interpretação de problemas;
- Capacidade de interpretação de um código legado;
- Capacidade de otimizar a resolução de problemas e;
- Resolver problemas/Otimizar algoritmos sob pressão.

## Instruções para instalar e rodar

<details>

1. Clone o repositório e entre na pasta:

    ```bash-shell
    git clone git@github.com:Ludson96/project-algorithms.git
    cd project-algorithms
    ```

1. Crie, ative e instale as dependências no ambiente virtual:

    ```bash-shell
    python3 -m venv .venv && source .venv/bin/activate
    python3 -m pip install -r dev-requirements.txt
    ```

1. Para rodar todos os testes utilize o comando:

    ```bash
    python3 -m pytest
    ```

1. Para rodar apenas em um arquivo:

    ```bash-shell
    python3 -m pytest <path do arquivo>
    ```

</details>

## Detalhamento das funções

Abaixo está uma lista das funções disponíveis.

<details>

### `study_schedule(permanence_period, target_time)`

- localizado em `challenges/challenge_study_schedule.py`

Essa função recebe uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída e um numero inteiro (`target_time`) que será o objetivo  de tempo a ser analisado como parâmetro, retorna a quantidade de pessoas estudantes estavam no sistema neste horário.

Exemplo de uso:

```python
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
students_quantity = study_schedule(permanence_period, 5)
```

Exemplo de retorno:

```md
# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
```

### `is_palindrome_recursive(word, low_index, high_index)`

- localizado em `challenges/challenge_palindromes_recursive.py`

Essa função recebe uma palavra (`word`), o menor index (`low_index`) e o maior index (`high_index`) como parametro. Verifica de forma recursiva se a palavra informada é um palíndromo e retorna um valor boolean (`True ou False`)

Exemplo de uso:

```python
word = "ANA"
is_palindrome_recursive(word, 0, 2)
# saída: True
word = "AGUA"
is_palindrome_recursive(word, 0, 3)
# saída: False
```

### `is_palindrome_iterative(word)`

- localizado em `challenges/challenge_palindromes_iterative.py`

Essa função recebe uma palavra (`word`). Verifica de forma iterativa se a palavra informada é um palíndromo e retorna um valor boolean (`True ou False`)

Exemplo de uso:

```python
word = "ANA"
is_palindrome_iterative(word)
# saída: True
word = "AGUA"
is_palindrome_iterative(word)
# saída: False
```

### `is_anagram(first_string, second_string)`

- localizado em `challenges/challenge_anagrams.py`

Essa função recebe duas palavra (`first_string` e `second_string`). Utiliza o algoritmo de ordenação `QuickSort` e compara as duas palavras, ordena e identifica se uma é um anagrama da outras. Retorna uma tupla com a primeira palavra, segunda palavra e um valor boolean (`True ou False`)

Exemplo de uso:

```python
first_string = "amor"
second_string = "roma"
is_anagram(first_string, second_string)
# saída: ('amor', 'amor', True)
# Explicação: Nesse caso a palavra 'amor' ordenada continua 'amor' e 'roma' ordenado vira 'amor, além disso a função é True, pois a palavra "roma" é um anagrama de "amor".
```

### `find_duplicate(nums)`

- localizado em `challenges/challenge_find_the_duplicate.py`

Essa função recebe uma lista de números inteiros no intervalo de [1, n] (`nums`). Utiliza o algoritmo de busca `Binário` e retorna apenas um número duplicado em nums.

Exemplo de uso:

```python
nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
find_duplicate(nums)
# saída: 7
```

</details>

[Git-logo]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[Python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Pytest-logo]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/
