# Установка зависимостей проекта
install:
	poetry install

# Запуск программ
gendiff:
	poetry run gendiff 'gendiff/file1.json' 'gendiff/file2.json'
#	poetry run gendiff

# Сборка проекта в whl файл
build:
	poetry build

# Публикация в PyPI (иммитация)
publish:
	poetry publish --dry-run

# Установка wheel файла
package-install:
	python3 -m pip install --force-reinstall dist/*.whl

# Проверка на lint
lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=python-project-lvl1 --cov-report xml

.PHONY: install test lint selfcheck check build gendiff