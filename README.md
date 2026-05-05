# Bootcamp Django Project

Привет. Это мой учебный проект на Django.

## Что тут есть

- `aggregator` — простая агрегация данных
- `local_government` — решения местных советов и их агрегация

## Что умеет API

### Aggregator

- `GET /api/aggregate/`
- `GET /api/aggregate/?group_by=source`

Считает:
- сумму
- среднее
- минимум
- максимум
- количество

### Local Government

- `GET /api/local-government/decisions/`
- `GET /api/local-government/decisions/aggregate/`
- `GET /api/local-government/decisions/aggregate/?group_by=category`

Считает:
- total_decisions
- total_budget

## Как запускать

1. Установить Django
2. Сделать миграции
3. Запустить сервер

Команды через make:

```bash
make migrate
make run
```

Тесты:

```bash
make test
```

## Админка

- `/admin/`

## Важно

Это очень простой проект для практики.
