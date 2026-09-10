# check.ps1 - скрипт для запуска всех проверок проекта

$ErrorActionPreference = "Stop"

function Write-Step($message) {
    Write-Host ""
    Write-Host "===> $message" -ForegroundColor Cyan
}

Write-Step "Black: проверка форматирования"
poetry run black --check src/ tests/

Write-Step "Isort: проверка порядка импортов"
poetry run isort --check-only src/ tests/

Write-Step "Flake8: проверка стиля"
poetry run flake8 src/ tests/

Write-Step "Mypy: проверка типов"
poetry run mypy src/

Write-Step "Pytest: тесты с покрытием"
poetry run pytest --cov=src tests/

Write-Host ""
Write-Host "Все проверки пройдены!" -ForegroundColor Green
