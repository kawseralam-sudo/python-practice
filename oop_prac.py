class Account:

    def __init__(self, account_number):
        self.account_number = account_number
        self.__balance = 0

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self.__balance:
            print("Error: Insufficient balance!")

        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def show_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance, "taka")


class Customer:

    def __init__(self, name, phone, account):
        self.name = name
        self.phone = phone
        self.account = account


class Bank:

    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


# ==========================
# Create Bank
# ==========================

bank = Bank()


# ==========================
# Create Account
# ==========================

print("========== CREATE ACCOUNT ==========")

name = input("Enter your name: ")
phone = input("Enter your phone number: ")

# Generate account number
account_number = "BD" + str(len(bank.customers) + 1001)

# Create account with balance 0
account = Account(account_number)

# Create customer
customer = Customer(name, phone, account)

# Add customer to bank
bank.add_customer(customer)


print("\nAccount created successfully!")

print("Name:", customer.name)
print("Phone:", customer.phone)

customer.account.show_balance()