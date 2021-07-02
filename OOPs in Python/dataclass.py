from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    price: float = field(default_factory=price_func)
    pages: int = 0

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}"

    def getbookinfo(self):
        return f"{self.title} by {self.author} costs {self.price}"

# b1 = Book('The Monk', 'Robin Sharma', 78.0, 250)
b1 = Book()
print(b1)
b2 = Book()
print(b2)
# print(b1.description)
