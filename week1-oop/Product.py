from typing import Union

class Product:
    def __init__(self,name: str, price: Union[int, float], stock:int):
        self.name = name
        self._price = price
        self._stock = stock

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, stock={self.stock})"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,val):
        if not isinstance(val, (int, float)):
            raise TypeError("Price must be a number")
        if val < 0:
            raise ValueError("Price cannot be negative")
        self._price = val

    @price.deleter
    def price(self):
        raise ValueError("Can't delete price,please update the price for product")

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("Stock must be a number")
        if val < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = val

    @stock.deleter
    def stock(self):
        self._stock = 0

class Cart:
    def __init__(self):
        self.cart = {}

    def add(self, product: Product, quantity: int):
        if quantity > product.stock:
            raise ValueError(f"Insufficient stock for {product.name}")
        self.cart[product] = quantity

    def __str__(self):
        if self.cart:
            return ' '.join(f'{i}:{j}' for i,j in self.cart.items())
        return f'No products in cart'
    
    def __len__(self):
        return len(self.cart)
    
    def __contains__(self, val):
        return val in self.cart

    def remove(self,product):
        if self.cart:
            try:
                pd = self.cart.pop(product)
            except KeyError:
                print(f'Please enter valid product name, {product} is not valid')
                return
            if pd:
                return f'Product: {product} has been removed'
        else:
            return f'Empty cart'

    @property
    def total(self):
        return sum(product.price * quantity for product, quantity in self.cart.items())

    @total.setter
    def total(self, val):
        raise AttributeError("Can't set total")
    
    @total.deleter
    def total(self):
        raise AttributeError("Can't delete total")
    

class Order:
    def __init__(self, cart: Cart):
        self.cart = cart
        self._status = "Pending"

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, val):
        raise AttributeError("Status cannot be set directly")  
    
    def place_order(self):
        # reduce stock for each product
        # set status to Placed
        if self._status == 'Cancelled':
            raise ValueError("Cannot place a cancelled order. Create a new order.")
        if self._status == 'Placed':
            print('Order has already been Placed')
            return
        for v, k in self.cart.cart.items():
            v.stock -= k
        self._status = 'Placed'

    def cancel_order(self):
        # restore stock for each product
        # set status to Cancelled
        if self.status != 'Cancelled':
            for v,k in self.cart.cart.items():
                v.stock += k
            self._status = "Cancelled"
        else:
            print('Order has already been cancelled')

laptop = Product("Laptop", 50000, 10)
phone = Product("Phone", 20000, 5)

cart = Cart()
cart.add(laptop, 2)
cart.add(phone, 1)

order = Order(cart)
print(order.status)      # Pending
order.place_order()
print(order.status)      # Placed
print(laptop.stock)      # 8
print(phone.stock)       # 4
order.cancel_order()
print(order.status)      # Cancelled
print(laptop.stock)      # 10
print(phone.stock)       # 5
order.cancel_order()
print(order.status)      # Cancelled
print(laptop.stock)      # 10
print(phone.stock)       # 5
order.place_order()
print(order.status)      # Placed
print(laptop.stock)      # 8
print(phone.stock)       # 4




