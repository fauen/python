import requests
from person import Person
from user import User, Work

p1 = Person('John', 'Doe', 35)
p2 = Person('Jane', 'Doe')

u1 = User('peter', 35)
#p3 = Person.occupation("Digger")


print(p1.firstname, p1.lastname, p1.age)
print(p2.firstname, p2.lastname, p2.age)
print(p1)
print(p2)
#print(p3)
print(u1)