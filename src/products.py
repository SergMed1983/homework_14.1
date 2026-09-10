class Product:
    """Класс для представления товара в интернет-магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация товара."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
