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

## Raspagem

Abaixo está uma lista das funções de raspagem disponíveis no arquivo `scraper.py`.

<details>

### `fetch(url)`

Essa função recebe uma URL como parâmetro, realiza uma solicitação GET na URL e retorna o conteúdo HTML da página.

Exemplo de uso:

```python
html_content = fetch("https://www.example.com")
```

### `scrape_updates(html_content)`

Essa função recebe o conteúdo HTML da página como parâmetro e retorna uma lista de links para as atualizações de notícias no site.

Exemplo de uso:

```python
news_links = scrape_updates(html_content)
```

### `scrape_next_page_link(html_content)`

Essa função recebe o conteúdo HTML da página como parâmetro e retorna o link para a próxima página de atualizações.

Exemplo de uso:

```python
next_page_link = scrape_next_page_link(html_content)
```

### `scrape_news(html_content)`

Essa função recebe o conteúdo HTML da página como parâmetro e retorna um dicionário com informações sobre uma notícia específica.

Exemplo de uso:

```python
news_info = scrape_news(html_content)
```

### `get_tech_news(n)`

Essa função recebe um número inteiro n como parâmetro e retorna uma lista com as últimas n notícias do site.

Exemplo de uso:

```python
latest_news = get_tech_news(10)
```

</details>

[Git-logo]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[Python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Pytest-logo]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white
[Pytest-url]: https://docs.pytest.org/en/7.2.x/
