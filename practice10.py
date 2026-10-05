products = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 800, "quantity": 5},
    {"name": "Keyboard", "price": 1500, "quantity": 3},
    {"name": "Monitor", "price": 12000, "quantity": 2},
    {"name": "Headphone", "price": 2500, "quantity": 4}
]

total_cost = 0


highest_price = products[0]["price"] * products[0]["quantity"]
highest_product = products[0]["name"]


lowest_price = products[0]["price"] * products[0]["quantity"]
lowest_product = products[0]["name"]


highest_quantity = products[0]["quantity"]
most_quantity_product = products[0]["name"]


for product in products:

    
    value = product["price"] * product["quantity"]

    print(product["name"], ":", value)

    
    total_cost += value

    
    if value > highest_price:
        highest_price = value
        highest_product = product["name"]

    
    if value < lowest_price:
        lowest_price = value
        lowest_product = product["name"]

   
    if product["quantity"] > highest_quantity:
        highest_quantity = product["quantity"]
        most_quantity_product = product["name"]


print()
print("Total Price:", total_cost)

print("Highest:", highest_product, highest_price)

print("Lowest:", lowest_product, lowest_price)

print("Most Quantity Product:", most_quantity_product)
print("Quantity:", highest_quantity)