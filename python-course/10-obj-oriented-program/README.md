# Chapter 10: Object-Oriented Programming (OOP)

---

## Classes and Objects

- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.
  
```python
class Person:
    pass

p1 = Person()  # p1 is an object of class Person
```

</br>

## Methods and Attributes

- **Attributes**: Variables that belong to a class/object.
- **Methods**: Functions that belong to a class.

```python
class Person:
    def __init__(self, name):
        self.name = name  # attribute

    def greet(self):      # method
        print(f"Hello, my name is {self.name}")

p = Person("Alice")
p.greet()
# __init__: Constructor method that runs when an object is created.
```