import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from products import Product  # noqa: E402
from categories import Category  # noqa: E402


def test_product_init():
    """Тест: корректная инициализация товара."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init():
    """Тест: корректная инициализация категории."""
    product1 = Product("Товар1", "Описание1", 100.0, 5)
    product2 = Product("Товар2", "Описание2", 200.0, 3)
    category = Category("Категория", "Описание категории", [product1, product2])

    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products) == 2
    assert category.products[0] == product1
    assert category.products[1] == product2


def test_category_count():
    """Тест: подсчёт количества категорий."""
    initial_count = Category.category_count

    # Создаём две категории (без присваивания — важны только побочные эффекты)
    Category("Кат1", "Описание1", [])
    Category("Кат2", "Описание2", [])

    assert Category.category_count == initial_count + 2


def test_product_count():
    """Тест: подсчёт количества товаров."""
    initial_count = Category.product_count

    products1 = [
        Product("Т1", "О1", 10, 1),
        Product("Т2", "О2", 20, 2)
    ]
    products2 = [
        Product("Т3", "О3", 30, 3)
    ]

    # Создаём категории (без присваивания)
    Category("Кат1", "Описание1", products1)
    Category("Кат2", "Описание2", products2)

    expected_count = initial_count + len(products1) + len(products2)
    assert Category.product_count == expected_count


def test_empty_category():
    """Тест: категория без товаров."""
    category = Category("Пустая", "Категория без товаров", [])
    assert len(category.products) == 0


def test_load_from_json_file_not_found():
    """Тест: файл не найден."""
    from loaders import load_data_from_json

    categories = load_data_from_json("несуществующий_файл.json")
    assert categories == []


def test_load_from_json_invalid_json():
    """Тест: некорректный JSON."""
    import tempfile
    import os
    from loaders import load_data_from_json

    # Создаём временный файл с некорректным JSON
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.json', delete=False, encoding='utf-8'
    ) as f:
        f.write("{ это не json :")
        temp_file_path = f.name

    try:
        categories = load_data_from_json(temp_file_path)
        assert categories == []
    finally:
        os.unlink(temp_file_path)


def test_load_from_json():
    """Тест: загрузка данных из JSON-файла."""
    import json
    import tempfile
    import os
    from loaders import load_data_from_json

    # Создаём временный JSON-файл с тестовыми данными
    test_data = {
        "categories": [
            {
                "name": "Тестовая категория",
                "description": "Описание теста",
                "products": [
                    {
                        "name": "Тестовый товар",
                        "description": "Описание товара",
                        "price": 100.0,
                        "quantity": 5
                    }
                ]
            }
        ]
    }

    # Создаём временный файл
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.json', delete=False, encoding='utf-8'
    ) as f:
        json.dump(test_data, f, ensure_ascii=False)
        temp_file_path = f.name

    try:
        # Загружаем данные
        categories = load_data_from_json(temp_file_path)

        # Проверяем результат
        assert len(categories) == 1
        assert categories[0].name == "Тестовая категория"
        assert categories[0].description == "Описание теста"
        assert len(categories[0].products) == 1
        assert categories[0].products[0].name == "Тестовый товар"
        assert categories[0].products[0].price == 100.0
        assert categories[0].products[0].quantity == 5

    finally:
        # Удаляем временный файл
        os.unlink(temp_file_path)
