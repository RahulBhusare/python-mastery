#Decorator examples
from functools import wraps

balance = {'Rahul':10000,'Jayashree':2000, 'Poonam':100000 , 'Raj':250000}
def log(func):
    @wraps(func) #when we use wraps tis will should actual function call name & doc string we can access it out side function.
    def wrapper(*args,**kwargs):
        """Wrapper to log"""
        print(f"Calling the {func.__name__}")
        res = func(*args,**kwargs)
        print(f"Done {func.__name__}")
        return res
    return wrapper


def validate_balance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        amt, from_acc = args[0], args[1]
        if amt <= 0:
            raise ValueError("Amount must be positive")
        if amt > balance[from_acc]:
            raise ValueError("Insufficient balance")
        return func(*args, **kwargs)  # just validate, don't update
    return wrapper

@validate_balance
@log
def transfer(amt, from_acc, to_acc):
    """Transfer amount between accounts"""
    balance[from_acc] -= amt      # update happens here
    balance[to_acc] += amt
    print(f"Transferred {amt} from {from_acc} to {to_acc}")

print(balance)
try:
    transfer(-100,"Rahul","Jayashree")
except ValueError as e:
    print(f'Error in transfer {e}')
print(balance)

print(transfer.__name__)  
print(transfer.__doc__)   