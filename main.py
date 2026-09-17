"""Точка входа для проверки ДЗ 14.1.

Позволяет запускать проект как из корня (`python main.py`),
так и из папки src (`python src/main.py`).
"""
import os
import sys

# Добавляем папку src в путь поиска модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from main import main  # noqa: E402


if __name__ == "__main__":
    main()
