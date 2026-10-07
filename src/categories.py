"""Модуль с классом Category."""

from src.products import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = list(products)

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию.
        Принимает только объекты Product или его наследников.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров категории.
        Если товаров нет — возвращает 0.
        """
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self) -> str:
        """Строковое отображение категории: общее количество товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        """Геттер: возвращает строку со всеми продуктами категории."""
        return "".join(f"{product}\n" for product in self.__products)
