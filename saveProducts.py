import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pive_ecommerce.settings")
django.setup()

from products.models import (
    Product,
)  # Zakładając, że masz model o nazwie Product w aplikacji products


def load_products_from_json():
    with open("products.json", "r") as file:
        products = json.load(file)

        for product_data in products:
            product = Product(
                id=product_data["id"],
                name=product_data["name"],
                stock=product_data["stock"],
                category=product_data["category"],
            )
            product.save()


if __name__ == "__main__":
    load_products_from_json()
