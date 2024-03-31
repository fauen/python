class Person:
    def __init__(self, firstname: str, lastname: str, age: int = None) -> None:
       self.firstname = firstname
       self.lastname = lastname 
       self.age = age
    
    def occupation(self, occupation):
        self.occupation = occupation