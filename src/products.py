from typing import Optional


class Product:
    """Класс для представления товара в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация товара."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(
        cls,
        product_data: dict,
        products_list: Optional[list["Product"]] = None,
    ):
        """
        Класс-метод: создаёт товар из словаря.
        Если передан products_list и товар с таким же именем уже есть —
        складывает количество и выбирает более высокую цену.
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if products_list is not None:
            for product in products_list:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер цены с проверкой положительного значения."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    def __str__(self) -> str:
        """Строковое отображение товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение двух товаров: суммарная стоимость (цена × количество)."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity
