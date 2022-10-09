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
