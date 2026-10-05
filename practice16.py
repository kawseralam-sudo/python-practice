orders = [
    {
        "customer": "Kawsar",
        "items": [
            {"name": "T-Shirt", "price": 650, "quantity": 2},
            {"name": "Jeans", "price": 1200, "quantity": 1}
        ]
    },
    {
        "customer": "Rahim",
        "items": [
            {"name": "Shoes", "price": 2500, "quantity": 1},
            {"name": "Cap", "price": 400, "quantity": 3}
        ]
    },
    {
        "customer": "Karim",
        "items": [
            {"name": "Laptop", "price": 50000, "quantity": 1},
            {"name": "Mouse", "price": 800, "quantity": 2}
        ]
    }
]

highest_bill = 0
highest_customer = ""

lowest_bill = 0
lowest_customer = ""

total_business_sales = 0
total_discount = 0
total_delivery = 0
final_business_revenue = 0

product_sales = {}

for order in orders:

    customer = order["customer"]
    total_bill = 0

    for item in order["items"]:

        total = item["price"] * item["quantity"]
        total_bill += total

        if item["name"] in product_sales:
            product_sales[item["name"]] += item["quantity"]
        else:
            product_sales[item["name"]] = item["quantity"]

    if total_bill >= 50000:
        discount = total_bill * 15 / 100
    elif total_bill >= 10000:
        discount = total_bill * 10 / 100
    elif total_bill >= 5000:
        discount = total_bill * 5 / 100
    else:
        discount = 0

    final_bill = total_bill - discount

    if final_bill >= 30000:
        delivery = 0
    elif final_bill >= 10000:
        delivery = 50
    else:
        delivery = 100

    final_pay = final_bill + delivery

    print("=============", customer, "=============")
    print("Total bill:", total_bill, "taka")
    print("Discount:", discount, "taka")
    print("Final bill:", final_bill, "taka")
    print("Delivery charge:", delivery, "taka")
    print("Final payable bill:", final_pay, "taka")
    print()

    if final_pay > highest_bill:
        highest_bill = final_pay
        highest_customer = customer

    if lowest_bill == 0 or final_pay < lowest_bill:
        lowest_bill = final_pay
        lowest_customer = customer

    total_business_sales += total_bill
    total_discount += discount
    total_delivery += delivery
    final_business_revenue += final_pay

most_sold_product = ""
most_sold_quantity = 0

for product, quantity in product_sales.items():

    if quantity > most_sold_quantity:
        most_sold_quantity = quantity
        most_sold_product = product

print("=========== BUSINESS SUMMARY ===========")

print("Highest Bill Customer:", highest_customer)
print("Highest Bill:", highest_bill)

print("Lowest Bill Customer:", lowest_customer)
print("Lowest Bill:", lowest_bill)

print("Most Sold Product:", most_sold_product)
print("Quantity Sold:", most_sold_quantity)

print("Total Business Sales:", total_business_sales)
print("Total Discount:", total_discount)
print("Total Delivery Charge:", total_delivery)
print("Final Business Revenue:", final_business_revenue)