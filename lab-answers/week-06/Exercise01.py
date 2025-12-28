"""
In example 2, a book is written by one and only one author. In reality, a book can be written by one or more authors.
Your task is to modify the Book class to support one or more authors by changing the instance variable authors to an Author array.

Some update:
The constructors take a list of Author (i.e., [author1, author2, ...]), instead of an Author instance. In this design, once a Book instance is constructed, you cannot add or remove an author.
A getAuthorNames() method returns "authorName1,authorName2,...".
The toString() method returns "Book[name=?,authors={Author[name=?,email=?,gender=?],......},price=?,qty=?]".
You are required to:

Write some updated code for the Book class. You should reuse the Author class in Example 2.
Note: You have to create a list of Author instances before you can construct an instance of Book.
"""

from typing import List

# author class
class Author:
    def __init__(self, name: str, email: str, gender: str):
        self.name = name
        self.email = email
        self.gender = gender

    def getName(self) -> str:
        return self.name

    def getEmail(self) -> str:
        return self.email

    def getGender(self) -> str:
        return self.gender

    def setEmail(self, email: str) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"Author[name = {self.name}, email = {self.email}, gender = {self.gender}]"

# book class
class Book:
    def __init__(self, name: str, authors: List[Author], price: float, qty: int = 0):
        self.name = name
        self.authors = authors
        self.price = price
        self.qty = qty

    def getName(self) -> str:
        return self.name

    def getAuthors(self) -> List[Author]:
        return self.authors

    def getPrice(self) -> float:
        return self.price

    def getQty(self) -> int:
        return self.qty

    def setPrice(self, price: float) -> None:
        self.price = price

    def setQty(self, qty: int) -> None:
        self.qty = qty
        
    def getAuthorNames(self) -> str:
        author_names = [author.getName() for author in self.authors]
        return ",".join(author_names)

    def __str__(self) -> str:
        authors_str = ", ".join([str(author) for author in self.__authors])
        return (f"Book[name = {self.name}, {{{authors_str}}}, price = {self.price}, qty = {self.qty}]")
