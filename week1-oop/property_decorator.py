from abc import ABC, abstractmethod 

class BankAccount(ABC):
    def __init__(self, account_holder, account_num, balance):
        self.account_holder = account_holder
        self.account_num = account_num
        self._balance = balance

    @abstractmethod
    def get_interest(self):
        pass

    def get_details(self, *args, **kwargs):
        details = f"BankAccount(account_holder='{self.account_holder}', account_num={self.account_num}, balance={self.balance})"
        details += ")"
        return details

    def deposit(self, amt):
        if not isinstance(amt, (int,float)):
              raise TypeError("Amount must be a number")
        if amt < 0:
            raise ValueError("Amount must be positive")
        self._balance += amt

    def withdraw(self,amt):
        if not isinstance(amt, (int, float)):
            raise TypeError("Amount must be a number")
        if amt < 0:
            raise ValueError("Amount must be positive")
        if amt > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amt

    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self, value):
        raise AttributeError("Balance cannot be set directly. Use deposit or withdraw methods.")
    
    @balance.deleter
    def balance(self):
        raise AttributeError("Balance cannot be deleted")
    
    def transfer(self, amt, tgt_acc):
        if not isinstance(amt, (int, float)):
            raise TypeError("Amount must be a number")
        if amt < 0:
            raise ValueError("Amount must be positive")
        if amt > self._balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amt)
        tgt_acc.deposit(amt)

    def __repr__(self):
        return f"BankAccount(account_holder='{self.account_holder}', account_num={self.account_num}, balance={self.balance})"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_num, balance, account_type):
        super().__init__(account_holder, account_num, balance)
        self.account_type = account_type

    def get_interest(self):
        # Placeholder implementation - replace with actual interest calculation logic
        int_rate =  self.balance * 0.04  # Example: 4% interest on the current balance
        return int_rate
    
    def get_details(self, show_interest=True, show_account_type=False):
        details = f"SavingsAccount(account_holder='{self.account_holder}', account_num={self.account_num}, balance={self.balance})"
        if show_account_type:
            details += f", account_type='{self.account_type}'"
        if show_interest:
            details += f", Interest={self.get_interest()}"
        details += ")"
        return details


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_num, balance, account_type):
        super().__init__(account_holder, account_num, balance)
        self.account_type = account_type

    def get_interest(self):
        # Placeholder implementation - replace with actual interest calculation logic
        return 0.0  # Current accounts typically do not earn interest

    def withdraw(self, amt):
        if not isinstance(amt, (int, float)):
            raise TypeError("Amount must be a number")
        if amt <= 0:
            raise ValueError("Amount must be positive")
        
        overdraft_limit = 10000
        if amt > self._balance + overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amt  # can go negative

    def get_details(self, show_interest=True, show_account_type=True):
        details = f"CurrentAccount(account_holder='{self.account_holder}', account_num={self.account_num}, balance={self.balance})"
        if show_account_type:
            details += f", account_type='{self.account_type}'"
        if show_interest:
            details += f", Interest={self.get_interest()}"
        details += ")"
        return details

# Example usage

rahul = SavingsAccount("Rahul", 1, 10000, "Savings")
priya = CurrentAccount("Priya", 2, 5000, "Current")
john = SavingsAccount("John", 3, 20000, "Savings")

accounts = [rahul, priya, john]
for acc in accounts:
    print(acc.get_details())

print(rahul.balance)
#rahul.balance = 15000  # This will raise an AttributeError

rahul.deposit(5000)
print(rahul.balance)

priya.withdraw(6000)  # This will work due to overdraft
print(priya.balance)    

