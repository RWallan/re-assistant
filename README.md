# Resident Evil Assistant

Resident Evil Assistant será uma biblioteca capaz de buscar dados do [Resident Evil Database](https://www.residentevildatabase.com/) e disponibilizar informações do mundo de Resident Evil através de uma interface de linha de comando (CLI).

## Objetivo

Disponibilizar um CLI que disponibiliza facilmente a interação do usuário com um modelo GPT especializado em Resident Evil. Podendo

- Interagir com o modelo via chat no CLI

- Aplicar um novo fine tuning no modelo

- Atualizar dados da database

## O que terá na v1

As metas a serem alcançadas são:

- [ ] Construir a base de dados contendo informações básicas dos [personagens disponíveis](https://www.residentevildatabase.com/personagens/) na database

- [ ] Construir uma base de treino para o fine tuning

- [ ] Aplicar fine tuning no modelo GPT

- [ ] Criar funções que possibilitam a conversação com o modelo

- [ ] Criar aplicação CLI para fácil interação o usuário

## Tecnologias

As tecnologias utilizadas no projeto são:

- [OpenAI](https://platform.openai.com/docs/overview) — API que permite comunicação com o GPT

- [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/#) — Para o Web Scraping

- [HTTPX](https://www.python-httpx.org/) — Para requisições assíncronas

E o [Poetry](https://python-poetry.org/docs/) para o gerenciamento de bibliotecas.

## Como utilizar

Ao fim do projeto, o usuário poderá utilizar o CLI da seguinte forma:

```bash
re-assistant get # Executa o pipeline para a aquisição dos dados
```

```bash
re-assistant train # Executa o pipeline de fine tuning do modelo
```

```bash
re-assistant chat # Inicia o chat com o assistant
```

## Como contribuir

O projeto estará sempre aberto a sugestões e contribuições. Para isso, você pode:

- Abrir uma issue

- Criar um fork e solicitar um Pull Request

## Licença

Este projeto está sob a licença MIT.

## TODOS

A lista de todos para que a primeira versão seja disponibilizada:

- [x] Construir descrição inicial do projeto

- [x] Inicializar repositório

- [x] Construir metadata o projeto

- [x] Organizar ambiente scrum

- [x] Criar método para buscar o catálogo de personagens

- [x] Criar método para buscar as informações básicas de cada personagem no catálogo

- [x] Persistir dados dos personagens

- [ ] Criar pipeline para construir os dados de exemplo para o fine tuning

- [ ] Criar pipeline de fine tuning

- [ ] Criar métodos para interagir com o modelo

- [ ] Criar CLI para interagir com o modelo

- [ ] Criar CLI para iniciar pipeline para buscar os dados da database

- [ ] Criar CLI para iniciar o pipeline de fine tuning

- [ ] Criar documentação completa do projeto
