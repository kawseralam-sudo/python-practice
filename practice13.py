cart = [
    {"name": "Rice", "price": 70, "quantity": 5},
    {"name": "Oil", "price": 180, "quantity": 2},
    {"name": "Sugar", "price": 120, "quantity": 3},
    {"name": "Milk", "price": 90, "quantity": 4},
    {"name": "Egg", "price": 12, "quantity": 12}
]
sub_total=0
for product in cart:
    total=product["price"]*product["quantity"]
    print(product["name"],":",total)
    sub_total+=total
    if sub_total>=1000:
        discount=100
    elif sub_total>=500:
        discount=50
    else:
        discount=0
final_bill=sub_total-discount
print("All products price:",sub_total)
print("You got:",discount,"taka discount")
print("After discount your price:",final_bill)
