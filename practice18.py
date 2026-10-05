accounts = [
    {
        "name": "Kawsar",
        "balance": 50000,
        "withdraw": 3000
    },
    {
        "name": "Rahim",
        "balance": 25000,
        "withdraw": 1000
    },
    {
        "name": "Karim",
        "balance": 15000,
        "withdraw": 2000
    }
]
with_succes=0
fail_count=0
succes_with_amount=0

for account in accounts:

    name = account["name"]
    balance = account["balance"]
    withdraw = account["withdraw"]

    print("==========", name, "==========")
    print("Balance:", balance)
    print("Withdraw:", withdraw)

    if balance >= withdraw:

        new_balance = balance - withdraw

        print("Withdrawal Successful")
        print("New Balance:", new_balance)
        with_succes+=1
        succes_with_amount+=withdraw
        
    else:

        print("Insufficient Balance")
        print("Withdrawal Failed")
        fail_count+=1
    print()

print("succesfull withdraw:",with_succes)
print("Failled withdraw:",fail_count)
print("succesfull withdraw net amount:",succes_with_amount)