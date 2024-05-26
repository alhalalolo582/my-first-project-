class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f} into account {}.".format(amount, self.account_number))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn ${:.2f} from account {}.".format(amount, self.account_number))
        else:
            print("Insufficient balance to withdraw ${:.2f} from account {}.".format(amount, self.account_number))

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Applied {:.2f}% interest to account {}.".format(self.interest_rate, self.account_number))

    def __str__(self):
        return "Account {}, Balance: ${:.2f}, Interest Rate: {:.2f}%".format(self.account_number, self.balance, self.interest_rate)

# Create an instance of BankAccount
account1 = BankAccount("56789", "Hala_1")
account1.deposit(1000)
print("Current balance: ${:.2f}".format(account1.get_balance()))
account1.withdraw(500)
print("Current balance: ${:.2f}".format(account1.get_balance()))

# Create an instance of SavingsAccount
savings_account = SavingsAccount("54321", "Hala_2", 3.5)
savings_account.deposit(2000)
print(savings_account)
savings_account.apply_interest()
print(savings_account)