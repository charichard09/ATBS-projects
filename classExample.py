class Person:
    "This is a perso class"
    age = 10

    def greet(self):
        print("Hello")

print(Person.age)

print(Person.greet)

print(Person.__doc__)