from products import Product


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
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Строковое отображение категории: общее количество товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        """Геттер: возвращает строку со всеми продуктами категории."""
        return "".join(f"{product}\n" for product in self.__products)
