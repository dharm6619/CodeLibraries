class Publicaion:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Book(Publicaion):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages
        # self.title = title
        # self.price = price

class Periodical(Publicaion):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,price)
        self.publisher = publisher
        self.period = period

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
        # self.title = title
        # self.publisher = publisher
        # self.price = price
        # self.period = period

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
        # self.title = title
        # self.publisher = publisher
        # self.price = price
        # self.period = period

b1 = Book("The Monk Who Sold His Ferrari", "Robin Sharma", 180, 150.0)
n1 = Newspaper("The Hindu", "The Hindu Times", 15.0, "Daily")
m1 = Magazine("India Today", "Nimbus", 50.0, "Monthly")

print(b1.title, n1.title, m1.title)
print(b1.author, n1.publisher, m1.publisher)
print(b1.price, n1.price, m1.price)