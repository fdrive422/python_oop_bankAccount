# create a BankAccount class with the attributes interest rate and balance
class BankAccount:
    def __init__(self, account_name, int_rate=0.004, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance

# add a deposit method to the BankAccount class
    def deposit(self, amount):
        self.account_balance += amount
        return self

# add a withdraw method to the BankAccount class
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient Funds: Charging $5 fee")
            self.account_balance = self.account_balance - 5
        else:
            self.account_balance -= amount
        return self

# add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(f"Current {self.account_name} {self.account_balance}")
        return self

# add a yield_interest method to the BankAccount class
    def yield_interest(self):
        self.account_balance += (self.account_balance * self.int_rate)
        return self

# create 2 account
checking = BankAccount('Checking',balance=1000)
savings = BankAccount('Savings',balance=2500)

# output/print beginning balances
print(f"Opening Checking: {checking.account_balance}")
print(f"Opening Savings: {savings.account_balance}")

# first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code
# second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code
checking.deposit(200).deposit(300).deposit(100).withdraw(200).yield_interest().display_account_info()
savings.deposit(500).deposit(500).withdraw(75).withdraw(75).withdraw(100).withdraw(100).yield_interest().display_account_info()
