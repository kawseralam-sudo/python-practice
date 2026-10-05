products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000},
    {"name": "Headphone", "price": 2500}
]

total_price = 0
highest_price =products[0]["price"]
lowest_price = products[0]["price"]
avove_count=0

for product in products:

    total_price += product["price"]

    if product["price"] > highest_price:
        highest_price = product["price"]

    if product["price"] < lowest_price:
        lowest_price = product["price"]
    if product["price"] >=500:
        avove_count+=1


print("Total price:",total_price)
print("The higest product price:",highest_price)
print("The lowest product price:",lowest_price)
print("Above 500 product:",avove_count)