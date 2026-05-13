#Library Management System

from typing import Union
class Book:
    def __init__(self, title: str , author:str, isbn:str, price:Union[int, float]):

        if not isinstance(title, str):
            raise TypeError('Title should be string')
        self.title = title
        
        if not isinstance(author, str):
            raise TypeError('Author should be String')
        self.author = author

        if not isinstance(isbn, str):
            raise TypeError('ISBN should be String')
        self._isbn = isbn
        
        if not isinstance(price, (int, float)):
            raise TypeError("Price should be positive number")
        self._price = price

    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        raise ValueError("Price Should not deleted")
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self,val):
        raise AttributeError("ISBN cannot be changed after creation")
    
    @isbn.deleter
    def isbn(self):
        raise AttributeError('ISBN cant be deleted')
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', price={self.price})"

    
    def __str__(self):
        return f"Book: {self.title}' by {self.author} | ISBN: {self.isbn} | Price: ₹{self.price}"
    
    def __eq__(self, other):
        if not isinstance(other,Book):
            return NotImplemented
        return self.isbn == other.isbn
        
    def __lt__(self, other):
        if not isinstance(other,Book):
            return NotImplemented
        return self.price < other.price
    
    
book1 = Book('Raj','ABC','ABC123',123)
book2 = Book('ShreeRaj','PQR','PQR123',122)
book3 = Book('Vidit','XYZ','XYZ123',123)
print(book1)
print(book1 == book2)
print(book1.author)
book1.author = 'Raj'
print(book1)
#del book1.isbn  # This is raise AttributeError
print(book1 < book2)