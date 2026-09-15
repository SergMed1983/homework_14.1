from products import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = list(products)  # приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию.
        Увеличивает счётчик продуктов на 1.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер: возвращает строку со всеми продуктами категории."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
