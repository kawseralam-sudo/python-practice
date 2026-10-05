accounts = [
    {
        "name": "Kawsar",
        "balance": 50000,
        "transactions": [
            {"type": "deposit", "amount": 10000},
            {"type": "withdraw", "amount": 5000},
            {"type": "withdraw", "amount": 8000}
        ]
    },

    {
        "name": "Rahim",
        "balance": 30000,
        "transactions": [
            {"type": "deposit", "amount": 5000},
            {"type": "withdraw", "amount": 12000},
            {"type": "deposit", "amount": 3000},
            {"type": "withdraw", "amount": 2000},
            {"type": "deposit", "amount": 4000}
        ]
    },

    {
        "name": "Karim",
        "balance": 80000,
        "transactions": [
            {"type": "withdraw", "amount": 20000},
            {"type": "deposit", "amount": 15000}
        ]
    }
]

highest_dep=0
highest_dep_name=""

lowest_dep=0
lowest_dep_name=""

highest_with=0
highest_with_name=""

lowest_with=0
lowest_with_name=""

most_transactions=0
most_active_customer=""

total_bank_dep=0
total_bank_with=0
total_bank_balance=0

highest_balance=0
highest_balance_name=""

for account in accounts:

    customer = account["name"]

    total_deposite = 0
    total_withdrow = 0
    transaction_count = 0

    for transaction in account["transactions"]:

        if transaction["type"] == "deposit":
            total_deposite += transaction["amount"]

        elif transaction["type"] == "withdraw":
            total_withdrow += transaction["amount"]

        transaction_count += 1

    final_balance=account["balance"]+total_deposite-total_withdrow

    print()
    print("============",customer,"=============")
    print("First balance:",account["balance"])
    print("Total Deposit:", total_deposite)
    print("Total Withdraw:", total_withdrow)
    print("Transactions:", transaction_count)
    print("Final balance:",final_balance)

    if total_deposite > highest_dep:
        highest_dep=total_deposite
        highest_dep_name=customer

    if lowest_dep==0 or total_deposite < lowest_dep:
        lowest_dep=total_deposite
        lowest_dep_name=customer

    if total_withdrow > highest_with:
        highest_with=total_withdrow
        highest_with_name=customer

    if lowest_with==0 or total_withdrow < lowest_with:
        lowest_with=total_withdrow
        lowest_with_name=customer

    if transaction_count > most_transactions:
     most_transactions = transaction_count
     most_active_customer = customer

    total_bank_dep+=total_deposite
    total_bank_with+=total_withdrow
    total_bank_balance+=final_balance

    if final_balance > highest_balance:
        highest_balance=final_balance
        highest_balance_name=customer

print()
print("=========================================")
print("             bank summery                ")
print("=========================================")
print()
print("Highest depositer name:",highest_dep_name)
print("Deposite amount:",highest_dep)
print()
print("Lowest depositer name:",lowest_dep_name)
print("Deposite amount:",lowest_dep)
print()
print("Highest withdrawal name:",highest_with_name)
print("Withdrow amount:",highest_with)
print()
print("Lowest withdrawl name:",lowest_with_name)
print("Withdrow amount:",lowest_with)
print()
print("Most active transaction name:",most_active_customer)
print("Total transaction:",most_transactions)
print()
print("Total bank deposite:",total_bank_dep)
print("Total bank withdrow:",total_bank_with)
print("Total bank balance:",total_bank_balance)
print()
print("Highest balance name:",highest_balance_name)
print("balance:",highest_balance)
