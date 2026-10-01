import pytest

from src.products import BaseProduct, Product


def test_base_product_is_abstract():
    """BaseProduct нельзя инстанцировать."""
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100, 1)


def test_repr_mixin_prints(capsys):
    """Миксин печатает информацию о создании."""
    Product("Продукт1", "Описание продукта", 1200, 10)
    captured = capsys.readouterr()
    assert "Product('Продукт1', 'Описание продукта', 1200, 10)" in captured.out
