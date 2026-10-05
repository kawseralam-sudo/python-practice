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


# ==========================================
# Global Variables
# ==========================================

highest_bill = 0
highest_customer = ""

lowest_bill = 0
lowest_customer = ""

total_business_sales = 0
total_discount = 0
total_delivery = 0
final_business_revenue = 0

# Product-এর total quantity রাখার জন্য
product_sales = {}


# ==========================================
# Customer Order Processing
# ==========================================

for order in orders:

    customer = order["customer"]

    customer_total = 0


    # --------------------------------------
    # প্রতিটি Product-এর Bill
    # --------------------------------------

    print()
    print("Customer:", customer)
    print("-----------------------------")

    for item in order["items"]:

        item_total = item["price"] * item["quantity"]

        print(
            item["name"],
            "→",
            item["price"],
            "x",
            item["quantity"],
            "=",
            item_total
        )

        customer_total += item_total


        # ----------------------------------
        # Product Quantity Count
        # ----------------------------------

        if item["name"] in product_sales:

            product_sales[item["name"]] += item["quantity"]

        else:

            product_sales[item["name"]] = item["quantity"]


    # --------------------------------------
    # Discount
    # --------------------------------------

    if customer_total >= 50000:

        discount = customer_total * 15 / 100

    elif customer_total >= 10000:

        discount = customer_total * 10 / 100

    elif customer_total >= 5000:

        discount = customer_total * 5 / 100

    else:

        discount = 0


    # --------------------------------------
    # Discount-এর পরের Bill
    # --------------------------------------

    after_discount = customer_total - discount


    # --------------------------------------
    # Delivery Charge
    # --------------------------------------

    if after_discount >= 30000:

        delivery = 0
        delivery_status = "Free Delivery"

    elif after_discount >= 10000:

        delivery = 50
        delivery_status = "Delivery Charge: 50"

    else:

        delivery = 100
        delivery_status = "Delivery Charge: 100"


    # --------------------------------------
    # Final Payable
    # --------------------------------------

    final_payable = after_discount + delivery


    # --------------------------------------
    # Print Customer Bill
    # --------------------------------------

    print("Total:", customer_total)
    print("Discount:", discount)
    print("After Discount:", after_discount)
    print("Delivery:", delivery_status)
    print("Final Payable:", final_payable)


    # --------------------------------------
    # Highest Bill
    # --------------------------------------

    if customer_total > highest_bill:

        highest_bill = customer_total
        highest_customer = customer


    # --------------------------------------
    # Lowest Bill
    # --------------------------------------

    if lowest_bill == 0 or customer_total < lowest_bill:

        lowest_bill = customer_total
        lowest_customer = customer


    # --------------------------------------
    # Business Statistics
    # --------------------------------------

    total_business_sales += customer_total

    total_discount += discount

    total_delivery += delivery

    final_business_revenue += final_payable


# ==========================================
# Most Sold Product
# ==========================================

most_sold_product = ""
most_sold_quantity = 0


for product, quantity in product_sales.items():

    if quantity > most_sold_quantity:

        most_sold_quantity = quantity
        most_sold_product = product


# ==========================================
# Final Business Summary
# ==========================================

print()
print("======================================")
print("        SHOPNEX BD SUMMARY")
print("======================================")

print()

print(
    "Highest Bill Customer:",
    highest_customer
)

print(
    "Highest Bill:",
    highest_bill
)

print()

print(
    "Lowest Bill Customer:",
    lowest_customer
)

print(
    "Lowest Bill:",
    lowest_bill
)

print()

print(
    "Most Sold Product:",
    most_sold_product
)

print(
    "Quantity Sold:",
    most_sold_quantity
)

print()

print(
    "Total Business Sales:",
    total_business_sales
)

print(
    "Total Discount:",
    total_discount
)

print(
    "Total Delivery Charge:",
    total_delivery
)

print(
    "Final Business Revenue:",
    final_business_revenue
)