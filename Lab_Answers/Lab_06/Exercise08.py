"""
Write the code for all the classes named Animal, Mammal, Cat, and Dog. 
"""

# animal class
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return f"Animal[{self.name}]"

# mammal subclass 
class Mammal(Animal):
    def __init__(self, name: str):
        super().__init__(name)
    
    def __str__(self) -> str:
        return f"Mammal[{super().__str__()}]"

# cat subclass
class Cat(Mammal):
    def __init__(self, name: str):
        super().__init__(name)
    
    def greets(self) -> None:
        print("Meow")
    
    def __str__(self) -> str:
        return f"Cat[{super().__str__()}]"
        
# dog subclass
class Dog(Mammal):
    def __init__(self, name: str):
        super().__init__(name)
    
    def greets(self, another=None) -> None:
        if another is None:
            print("Woof")
        elif isinstance(another, Dog):
            print("Woooof")
        
    def __str__(self) -> str:
        return f"Dog[{super().__str__()}]"
