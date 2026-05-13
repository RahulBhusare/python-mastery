from abc import ABC, abstractmethod 

class BankAccount(ABC):
    def __init__(self, account_holder, account_num, balance):
        self.account_holder = account_holder
        self.account_num = account_num
        self._balance = balance

    def __str__(self):
        return f"BankAccount of {self.account_holder} with account number {self.account_num} has a balance of {self.balance}"
    
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.account_num == other.account_num
    
    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance
    
    @abstractmethod
    def get_interest(self):
        pass

    def get_details(self, *args, **kwargs):
        details = f"BankAccount(account_holder='{self.account_holder}', account_num={self.account_num}, balance={self.balance})"
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

if __name__ == "__main__":
    acc1 = SavingsAccount("Rahul", 1, 10000, "Savings")
    acc2 = SavingsAccount("Priya", 1, 5000, "Savings")
    acc3 = SavingsAccount("John", 2, 20000, "Savings")

    print(str(acc1))        # user friendly
    print(repr(acc1))       # developer friendly
    print(acc1 == acc2)     # True - same account_num
    print(acc1 == acc3)     # False - different account_num
    print(acc1 < acc3)      # True - acc1 balance < acc3 balance

    # Sorting by balance
    accounts = [acc1, acc3, acc2]
    print(sorted(accounts))  # sorted by balance
    print(acc1.get_details(show_interest=True, show_account_type=True))
    acc1.deposit(5000)
    print(acc1.balance)          # 15000        
    acc1.withdraw(2000)
    print(acc1.balance)          # 13000

    #acc1.balance = 123         #This is raise exception
    print(acc1)
    