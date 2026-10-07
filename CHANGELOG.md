# Changelog

## [16.1] - 2026-09-24

### Добавлено
- Классы-наследники `Smartphone` и `LawnGrass` от `Product`:
  - `Smartphone`: атрибуты `efficiency`, `model`, `memory`, `color`.
  - `LawnGrass`: атрибуты `country`, `germination_period`, `color`.
- Ограничение сложения товаров по типу через `type()` в `Product.__add__`:
  складывать можно только объекты одного класса, иначе — `TypeError`.
- Проверка типа в `Category.add_product` через `isinstance`:
  принимаются только `Product` и его наследники, иначе — `TypeError`.
- Тесты на новую функциональность.

### Изменено
- `Product.__add__` вместо `isinstance` использует `type()`.
- Тесты обновлены: `test_product_add_invalid_type` теперь ожидает `TypeError`.

### Тесты
- 37 тестов, покрытие 100%.

## [14.2] - 2026-09-15

### Добавлено
- Приватный атрибут `__products` в классе `Category`.
- Метод `add_product()` для добавления товаров в категорию.
- Геттер `products` через `@property` — возвращает строку со всеми товарами.
- Класс-метод `Product.new_product()` для создания товара из словаря.
- Приватный атрибут `__price` и геттер/сеттер `price` в классе `Product`.
- Проверка положительной цены в сеттере.

### Изменено
- `loaders.py` использует `Product.new_product()` при загрузке из JSON.
- `main.py` адаптирован под строковый геттер `products`.
- Тесты обновлены под новую функциональность.
- 