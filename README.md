## Инструменты качества кода

- `flake8` — линтинг
- `black` — форматирование
- `isort` — сортировка импортов
- `mypy` — проверка типов
- `pytest` + `pytest-cov` — тестирование с покрытием

Все проверки запускаются одной командой:

```powershell
.\check.ps1
```

## Отчёт о покрытии тестами

Покрытие `src/` — **100%** (37 тестов, требование — более 75%).

```
Name                Stmts   Miss  Cover
---------------------------------------
src\categories.py      21      0   100%
src\loaders.py         18      0   100%
src\products.py        48      0   100%
---------------------------------------
TOTAL                  87      0   100%
```

Подробный HTML-отчёт: [`htmlcov/index.html`](htmlcov/index.html)

Сгенерировать заново:

```bash
poetry run pytest --cov=src --cov-report=html
```
