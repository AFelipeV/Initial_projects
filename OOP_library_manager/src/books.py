class Book:

    counter = 0

    def __init__(self, name, author, year, isbn):
        self.name = name
        self.author = author
        self.year = year
        self.isbn = isbn
        Book.counter += 1

    def __str__(self):
        return f"The book '{self.name}' was written by {self.author} in {self.year} and published with ISBN {self.isbn}."

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year,
            "ISBN": self.isbn
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            author=data["author"],
            year=data["year"],
            isbn=data["ISBN"]
        )

    @classmethod
    def get_counter(cls):
        return cls.counter
