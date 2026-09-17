import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from categories import Category  # noqa: E402
from products import Product  # noqa: E402


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
    assert "Товар1, 100.0 руб. Остаток: 5 шт." in category.products
    assert "Товар2, 200.0 руб. Остаток: 3 шт." in category.products


def test_category_count():
    """Тест: подсчёт количества категорий."""
    initial_count = Category.category_count

    Category("Кат1", "Описание1", [])
    Category("Кат2", "Описание2", [])

    assert Category.category_count == initial_count + 2


def test_product_count():
    """Тест: подсчёт количества товаров."""
    initial_count = Category.product_count

    products1 = [Product("Т1", "О1", 10, 1), Product("Т2", "О2", 20, 2)]
    products2 = [Product("Т3", "О3", 30, 3)]

    Category("Кат1", "Описание1", products1)
    Category("Кат2", "Описание2", products2)

    expected_count = initial_count + len(products1) + len(products2)
    assert Category.product_count == expected_count


def test_empty_category():
    """Тест: категория без товаров."""
    category = Category("Пустая", "Категория без товаров", [])
    assert category.products == ""


# ---------- Тесты 14.2 ----------


def test_add_product():
    """Тест: добавление продукта через add_product()."""
    category = Category("Фрукты", "Свежие", [])
    initial_count = Category.product_count

    product = Product("Яблоко", "Свежее", 80, 15)
    category.add_product(product)

    assert "Яблоко, 80 руб. Остаток: 15 шт." in category.products
    assert Category.product_count == initial_count + 1


def test_add_product_returns_none():
    """Тест: add_product() не возвращает значения."""
    category = Category("Фрукты", "Свежие", [])
    product = Product("Яблоко", "Свежее", 80, 15)
    assert category.add_product(product) is None


def test_products_getter_format():
    """Тест: точный формат строки геттера products."""
    product = Product("Яблоко", "Свежее", 80, 15)
    category = Category("Фрукты", "Свежие", [product])
    assert category.products == "Яблоко, 80 руб. Остаток: 15 шт.\n"


def test_price_getter():
    """Тест: геттер цены возвращает значение."""
    product = Product("Яблоко", "Свежее", 80, 15)
    assert product.price == 80


def test_price_setter_valid():
    """Тест: сеттер устанавливает положительную цену."""
    product = Product("Яблоко", "Свежее", 80, 15)
    product.price = 100
    assert product.price == 100


def test_price_setter_invalid_zero(capsys):
    """Тест: сеттер не принимает нулевую цену."""
    product = Product("Яблоко", "Свежее", 80, 15)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 80


def test_price_setter_invalid_negative(capsys):
    """Тест: сеттер не принимает отрицательную цену."""
    product = Product("Яблоко", "Свежее", 80, 15)
    product.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 80


def test_new_product():
    """Тест: класс-метод new_product создаёт товар из словаря."""
    data = {"name": "Груша", "description": "Сладкая", "price": 120, "quantity": 10}
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Груша"
    assert product.description == "Сладкая"
    assert product.price == 120
    assert product.quantity == 10


def test_new_product_with_duplicate():
    """Тест: new_product складывает количество дубликата и берёт max цену."""
    existing = Product("Яблоко", "Свежее", 80, 10)
    data = {"name": "Яблоко", "description": "Свежее", "price": 100, "quantity": 5}

    result = Product.new_product(data, [existing])

    assert result is existing
    assert result.quantity == 15
    assert result.price == 100


def test_new_product_with_duplicate_lower_price():
    """Тест: при дубликате с меньшей ценой остаётся старая цена."""
    existing = Product("Яблоко", "Свежее", 100, 10)
    data = {"name": "Яблоко", "description": "Свежее", "price": 80, "quantity": 5}

    result = Product.new_product(data, [existing])

    assert result.quantity == 15
    assert result.price == 100


# ---------- Тесты loaders ----------


def test_load_from_json_file_not_found():
    """Тест: файл не найден."""
    from loaders import load_data_from_json

    categories = load_data_from_json("несуществующий_файл.json")
    assert categories == []


def test_load_from_json_invalid_json():
    """Тест: некорректный JSON."""
    import tempfile

    from loaders import load_data_from_json

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
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

    from loaders import load_data_from_json

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
                        "quantity": 5,
                    }
                ],
            }
        ]
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False)
        temp_file_path = f.name

    try:
        categories = load_data_from_json(temp_file_path)

        assert len(categories) == 1
        assert categories[0].name == "Тестовая категория"
        assert categories[0].description == "Описание теста"
        assert "Тестовый товар, 100.0 руб. Остаток: 5 шт." in categories[0].products
    finally:
        os.unlink(temp_file_path)


# ---------- Новые тесты 15.1 ----------


def test_product_str():
    """Тест: строковое отображение товара."""
    product = Product("Яблоко", "Свежее", 80, 15)
    assert str(product) == "Яблоко, 80 руб. Остаток: 15 шт."


def test_category_str():
    """Тест: строковое отображение категории — общее количество товаров."""
    product1 = Product("Яблоко", "Свежее", 80, 15)
    product2 = Product("Груша", "Сладкая", 120, 10)
    category = Category("Фрукты", "Свежие фрукты", [product1, product2])
    assert str(category) == "Фрукты, количество продуктов: 25 шт."


def test_category_str_empty():
    """Тест: строковое отображение пустой категории."""
    category = Category("Пустая", "Без товаров", [])
    assert str(category) == "Пустая, количество продуктов: 0 шт."


def test_product_add():
    """Тест: сложение двух товаров возвращает суммарную стоимость."""
    a = Product("Товар A", "Описание", 100, 10)
    b = Product("Товар B", "Описание", 200, 2)
    assert a + b == 1400


def test_product_add_zero_quantity():
    """Тест: сложение с нулевым количеством."""
    a = Product("Товар A", "Описание", 100, 0)
    b = Product("Товар B", "Описание", 200, 2)
    assert a + b == 400


def test_product_add_invalid_type():
    """Тест: сложение с не-Product возвращает NotImplemented."""
    a = Product("Товар A", "Описание", 100, 10)
    assert a.__add__(5) is NotImplemented
