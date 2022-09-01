number_of_orders = int(input())

total_amount = 0
for _ in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())
    if 0.01 <= price_capsule <= 100.00 \
            and 1 <= days <= 31 \
            and 1 <= caps_per_day <= 2000:
        order_total = price_capsule * days * caps_per_day
        total_amount += order_total
        print(f"The price for the coffee is: ${order_total:.2f}")

print(f"Total: ${total_amount:.2f}")
