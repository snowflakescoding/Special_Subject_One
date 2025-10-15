"""
A class called Book is designed (as shown in the class diagram) to model a book written by a single author. It contains:
Four private instance variables: name (String), author (of the class Author, you have just created, assume that a book has one and only one author), price (double), and qty (int) with a default value of 0.
Two constructors with qty and without qty.
A toString() that returns "Book[name=?,Author[name=?,email=?,gender=?],price=?,qty=?". You should reuse the Author’s toString().

Write Python code for the Author and Book class.
Note: You have to construct an instance of Author before you can construct an instance of Book.
"""

# author class
class Author:
    # init function
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    # getter and setter
    def getName(self):
        return self.name

    def getEmail(self):
        return self.email
    
    def getGender(self):
        return self.gender

    def setEmail(self, email):
        self.email = email

    # string function
    def __str__(self):
        return f"Author[name = {self.name}, email = {self.email}, gender = {self.gender}]"

# book function
class Book:
    # init function
    def __init__(self, name, author, price, qty=0):
        self.name = name
        self.author = author 
        self.price = price
        self.qty = qty
    
    # getter and setter
    def getName(self):
        return self.name
        
    def getAuthor(self):
        return self.author
        
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
        
    def getQty(self):
        return self.qty

    def setQty(self, qty):
        self.qty = qty

    # string function
    def __str__(self):
        author_str = str(self.author)
        return f"Book[name = {self.name}, {author_str}, price = {self.price}, qty = {self.qty}]"
