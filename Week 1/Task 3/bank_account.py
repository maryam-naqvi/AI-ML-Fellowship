class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New Balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        
        return f"Account Owner: {self.owner}, Balance: ${self._balance}"


class SavingsAccount(BankAccount): 
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest of ${interest}")


if __name__ == "__main__":
    print("--- Bank Account System ---")
    acc = SavingsAccount("Maryam", 1000)
    print(acc)        
    acc.deposit(500)
    acc.withdraw(200)
    acc.apply_interest()
    print(acc)