"""Модуль с классом Product и его наследниками."""

from abc import ABC, abstractmethod
from typing import Optional


class ReprMixin:
    """
    Миксин, который при создании объекта выводит в консоль
    информацию о том, от какого класса и с какими параметрами он создан.
    """

    def __init__(self, *args, **kwargs):
        # Вызываем super(), чтобы цепочка наследования продолжилась
        super().__init__(*args, **kwargs)

        # Формируем строку с аргументами для логирования
        params = ", ".join(repr(arg) for arg in args)
        if kwargs:
            kw_params = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            params = f"{params}, {kw_params}" if params else kw_params

        # Печатаем в консоль (используем __class__.__name__ для имени класса)
        print(f"{self.__class__.__name__}({params})")


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Общая инициализация для всех продуктов."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass


class Product(ReprMixin, BaseProduct):
    """
    Класс для представления товара в интернет-магазине.
    Наследуется от ReprMixin (для логирования) и BaseProduct (для общего интерфейса).
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация товара."""
        super().__init__(name, description, price, quantity)

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

    def __str__(self) -> str:
        """Строковое отображение товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение двух товаров: суммарная стоимость (цена * количество).
        Разрешено только между объектами одного и того же класса.
        """
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать товары разных классов: " f"{type(self).__name__} и {type(other).__name__}"
            )
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс-наследник: смартфон."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс-наследник: трава газонная."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
