from dunder_methods import BankAccount, SavingsAccount, CurrentAccount

class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_types = {"savings": SavingsAccount, "current": CurrentAccount}

    def create_account(self,acc_type, account_holder, account_num, balance, rate):
        if acc_type in self.account_types:
            account_class = self.account_types[acc_type]
            account = account_class(account_holder, account_num, balance, rate)
        else:
            raise ValueError("Invalid account type")
        self.accounts[account_num] = account
        return account
    
    def get_account(self,acc_num):
        if self.accounts.get(acc_num) is None:
            raise ValueError("Account not found")
        return self.accounts[acc_num]
    
    def transfer(self, amt, src_acc_num, tgt_acc_num):
        src_acc = self.get_account(src_acc_num)
        tgt_acc = self.get_account(tgt_acc_num)
        src_acc.transfer(amt, tgt_acc)

    def deposit(self, amt, acc_num):
        acc = self.get_account(acc_num)
        acc.deposit(amt)

    def withdraw(self, amt, acc_num):
        acc = self.get_account(acc_num)
        acc.withdraw(amt)

    def sort_accounts_by_balance(self):
        return sorted(self.accounts.values())
    
    def total_deposits(self):
        return sum(acc.balance for acc in self.accounts.values())
    
bank = Bank()
account1 = bank.create_account("savings", "John Doe", 1, 1000, 0.02)
account2 = bank.create_account("current", "Rahul", 2, 200, 0.03)
account1.deposit(500)
print(f'bank.total_deposits()): {bank.total_deposits()}')  # Output: 3300
sorted_accounts = bank.sort_accounts_by_balance()
print(f"Accounts sorted by balance:{sorted_accounts}")
print(f"Bank accounts: {bank.accounts}")
bank.transfer(300, 1, 2)
print(f"Account 1 balance: {account1.balance}")  # Output: 12000
print(f"Account 2 balance: {account2.balance}")  # Output: 8000
bank.withdraw(100, 2)
print(f"Account 2 balance after withdrawal: {account2.balance}")  # Output: 7900            

