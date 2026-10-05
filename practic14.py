order = [
    {"name": "T-Shirt", "price": 650, "quantity": 2},
    {"name": "Jeans", "price": 120, "quantity": 1},
    {"name": "Shoes", "price": 250, "quantity": 1},
    {"name": "Cap", "price": 400, "quantity": 3}
]

total = 0

# প্রতিটি product-এর subtotal
for product in order:

    subtotal = product["price"] * product["quantity"]

    print(
        product["name"],
        "→",
        product["price"],
        "x",
        product["quantity"],
        "=",
        subtotal
    )

    total += subtotal


# Discount
if total >= 5000:
    discount = total * 10 / 100

elif total >= 3000:
    discount = total * 5 / 100

else:
    discount = 0


# Discount বাদ দেওয়ার পর
final_bill = total - discount


# Delivery charge
if final_bill >= 5000:
    delivery = 0
    delivery_status = "Free Delivery"

else:
    delivery = 100
    delivery_status = "Delivery Charge: 100"


# Final payable
payable = final_bill + delivery


print()
print("========== SHOPNEX BD BILL ==========")
print("Total:", total)
print("Discount:", discount)
print("After Discount:", final_bill)
print("Delivery:", delivery_status)
print("Final Payable:", payable)