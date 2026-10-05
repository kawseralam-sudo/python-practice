def cal_total_price(price, quantity):

    return price * quantity


def cart_total(cart):

    total = 0

    for item in cart:

        item_total = cal_total_price(
            item["price"],
            item["quantity"]
        )

        print(item["name"], ":", item_total)

        total += item_total

    return total


def cal_discount(total):

    if total >= 1000:
        return total * 10 / 100
    else:
        return 0


cart = [
    {"name": "Rice", "price": 70, "quantity": 5},
    {"name": "Oil", "price": 180, "quantity": 2},
    {"name": "Sugar", "price": 120, "quantity": 3},
    {"name": "Milk", "price": 90, "quantity": 4}
]


total = cart_total(cart)

discount = cal_discount(total)

final_price = total - discount


print("Total:", total)
print("Discount:", discount)
print("Final Price:", final_price)