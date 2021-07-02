class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is my secret"
    
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount

b1 = Book("The Monk Who Sold His Ferrari", "Robin Sharma", 150, 200)
print(b1)
print(b1.get_price())
b1.setdiscount(0.10)
print(b1.get_price())
print(b1._Book__secret)
