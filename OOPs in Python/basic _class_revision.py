class Book:
    BOOK_TYPES = ("Hardcover", "Paperback", "EBook")
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    def set_title(self, title):
        self.title = title
    
    def __init__(self,title,booktype):
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} not in {Book.BOOK_TYPES}")
        else:
            self.booktype=booktype
        self.title = title

print(Book.get_book_types())
b1 = Book("The Monk Who Sold His Ferrari", "Hardcover")
b2 = Book("The Monk Who Sold His Ferrari", "Paperback")
