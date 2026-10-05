products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000},
    {"name": "Headphone", "price": 2500}
]

for product in products:

    price = product["price"]

    if price >= 10000:
        discount = price * 10 / 100

    elif price >= 5000:
        discount = price * 5 / 100

    else:
        discount = 0

    final_price = price - discount

    print(
        product["name"],
        "→ Original:", price,
        "→ Discount:", discount,
        "→ Final:", final_price
    )