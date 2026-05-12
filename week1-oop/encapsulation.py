class BankAccount:
    def __init__(self, account_holder, account_num, balance, rate):
        self.account_holder = account_holder
        self.account_num = account_num
        self.__balance = balance
        self.__rate = rate

    def deposit(self, amt):
        if not isinstance(amt, (int,float)):
              raise TypeError("Amount must be a number")
        if amt < 0:
            raise ValueError("Amount must be positive")
        self.__balance += amt
    
    def withdraw(self,amt):
        if not isinstance(amt, (int, float)):
            raise TypeError("Amount must be a number")
        if amt < 0:
            raise ValueError("Amount must be positive")
        if amt > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amt

    def get_balance(self):
        return self.__balance
    
    def get_rate(self):
        return self.__rate
    
    def transfer(self, amt, tgt_acc):
        if not isinstance(amt, (int, float)):
            raise TypeError("Amount must be a number")
        if amt < 0:
            raise ValueError("Amount must be positive")
        if amt > self.__balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amt)
        tgt_acc.deposit(amt)

account = BankAccount("John Doe", 1, 1000, 0.02) 
account1 = BankAccount("Rahul", 2, 2000, 0.03)
account.deposit(500)
print(f'account.get_balance()): {account.get_balance()}')  # Output: 1500
account.withdraw(200)
print(f'account.get_balance()): {account.get_balance()}')  # Output: 1300
# The following line will raise an error because __balance is private
#print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance' 
#   The correct way to access the balance is through the get_balance method
print(f'account.get_balance()): {account.get_balance()}')  # Output: 1300  
# The following line will raise an error because __balance is private
#account.__balance = 5000  # AttributeError: 'BankAccount' object has no attribute '__balance' 
# The correct way to modify the balance is through the deposit and withdraw methods
account.deposit(500)  # This will add 500 to the balance
print(f'account.get_balance()): {account.get_balance()}')  # Output: 1800
#print(account.__rate)  # Output: 0.05
account.transfer(300, account1)  # This will transfer 300 from John's account to Rahul's account
print(f'account.get_balance()): {account.get_balance()}')  # Output: 1500
print(f'account1.get_balance()): {account1.get_balance()}')  # Output: 2300
print(f'account.get_rate()): {account.get_rate()}')  # Output: 0.02
