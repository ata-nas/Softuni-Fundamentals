PRODUCT_COFFEE = "coffee"
PRODUCT_WATER = "water"
PRODUCT_COKE = "coke"
PRODUCT_SNACKS = "snacks"
PRICE_COFFEE = 1.50
PRICE_WATER = 1.00
PRICE_COKE = 1.40
PRICE_SNACKS = 2.00


def order_total(product: str, quantity: int):
    result = None
    if product == PRODUCT_COFFEE:
        result = PRICE_COFFEE * quantity
    elif product == PRODUCT_WATER:
        result = PRICE_WATER * quantity
    elif product == PRODUCT_COKE:
        result = PRICE_COKE * quantity
    elif product == PRODUCT_SNACKS:
        result = PRICE_SNACKS * quantity
    return result


user_product = input()
user_quantity = int(input())

total = order_total(user_product, user_quantity)

print(f"{total:.2f}")
