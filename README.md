# Django Bootcamp

Простий навчальний проєкт на Django.

## Додаток

- `local_government` — облік рішень місцевих рад і зведена статистика

## API

- `GET /api/local-government/decisions/`
- `GET /api/local-government/decisions/?limit=50&offset=0`
- `GET /api/local-government/decisions/aggregate/`
- `GET /api/local-government/decisions/aggregate/?group_by=category`

## Запуск

```bash
make migrate
make run
```

## Тести

```bash
make test
```
