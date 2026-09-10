import json

from categories import Category
from products import Product


def load_data_from_json(file_path: str):
    """
    Загружает данные из JSON-файла и создаёт объекты Category и Product.

    Args:
        file_path: путь к JSON-файлу

    Returns:
        list[Category]: список созданных категорий
    """
    categories_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for category_data in data.get("categories", []):
            products = []
            for product_data in category_data.get("products", []):
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
            categories_list.append(category)

    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON")

    return categories_list
