PYTHON=python3
MANAGE=$(PYTHON) manage.py

# Створити та застосувати міграції.
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Запустити локальний сервер.
run:
	$(MANAGE) runserver

# Запустити всі тести.
test:
	$(MANAGE) test
