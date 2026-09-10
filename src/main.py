from loaders import load_data_from_json
from categories import Category


def main():
    categories = load_data_from_json('products.json')

    if not categories:
        print("Не удалось загрузить данные из JSON")
        return

    print("=" * 50)
    print("ЗАГРУЖЕННЫЕ КАТЕГОРИИ")
    print("=" * 50)

    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товаров в категории: {len(category.products)}")
        print("Товары:")
        for product in category.products:
            print(f"  - {product.name}: {product.price} руб. (в наличии: {product.quantity} шт.)")

    print("\n" + "=" * 50)
    print("СТАТИСТИКА")
    print("=" * 50)
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
