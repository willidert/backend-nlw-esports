# NLW 09 - versão [drf](https://www.django-rest-framework.org/)

Um projeto desenvolvido durante a nona edição da NLW, evento online e gratuito promovido pela Rocketseat.

## Features

- A api disponibiliza uma lista de games
- `Game` possui: `id`, `bannerUrl` e `title`
- `Game` possui nenhum ou muitos `Ad`'s
- É possivel `criar` e `listar` `Ad`'s associados a um `Game`
- `Ad` possui: `id`, `game`, `name`, `weekDays`, `yearsPlaying`, `hourStart`, `hourEnd`, `useVoiceChannel` e `discord`.
- É possível exibir o discord associado a um `Ad`

## Tecnologias

| tecnlogia             |                                                                                                            descrição                                                                                                             |
| --------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Django                | O Django é um framework para desenvolvimento de aplicações web com Python que trabalha com uma arquitetura MVC. Entretanto `Views` no Django se referem a "controllers" e `templates` se referem a "views", apenas nomenclatura. |
| SQLite                |                        É um banco de dados leve usado principalmente para pequenas aplicações, usado aqui para facilitar a execução do projeto. O ideal seria utilizar containers com PostgreSQL ou MySQL                        |
| django rest framework |                                                                         É uma biblioteca baseada para desenvolvimento de REST api's utilizando o Django.                                                                         |

## Execução

Clonar o projeto:

```sh
git clone <url>
cd backend-nlw-09-esports/python
```

Recomendo a utilização de um ambiente virtual para execução:

```sh
# isso criará um ambiente virtual chamado "env", você pode colocar o nome que desejar
python -m venv env
source env/bin/activate # ativar o ambiente

pip install -R requirements.txt
```

Após a instalação das dependências, o projeto pode ser executado:

```sh
python manage.py runserver
```

E a api estará rodando na porta padrão, 8000, do django. Você pode mudar essa porta se desejar (ver documentação do Django). O drf disponibiliza uma interface para visualização da api mas eu recomenda utilizar um cliente como postman ou insomnia, para vs code existem extensões, recomendo a thunderclient.

## Testes

Utilizei a Pytest por ser mais simples que as ferramentas de teste do Django, apesar de ainda não compreender totalmente os contextos de uso. Os testes estão organizados em uma pasta tests dentro do app, cada arquivo de teste está relacionado com um contexto especifico, é a tentativa pelo menos. Muitos dos testes foram baseados em outros projetos, ainda tenho dificuldade em criar cenários de teste reais que possam quebrar ou pelo menos mostrar bugs.

Para executar os testes:

```sh
coverage run -m pytest
```

Ou

```sh
pytest
```

Os percentuais exibidos no output da pytest se referem ao progresso dos testes e não à cobertura. Para isso uso a coverage, mais adiante, tenha em mente que a coverage precisa capturar o output da pytest, então é necessário executar ao menos uma vez com `coverage run` antes de:

```sh
coverage report -m
```

A opção `-m` é para exibir a quantidade de declarações não executadas.
