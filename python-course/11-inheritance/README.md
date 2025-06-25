# Chapter 11: Inheritance & More on OOPs

### 1. Inheritance

* **Definition:** Mechanism where a new class (child/subclass) derives properties and behaviors (attributes and methods) from an existing class (parent/superclass).
* **Purpose:** Code reuse, logical hierarchy, and extensibility.
* **Syntax:**

  ```python
  class Parent:
      # parent code

  class Child(Parent):
      # child inherits from Parent
  ```
* **Types:**

  * Single Inheritance: One parent class.
  * Multiple Inheritance: Child inherits from multiple parents.
  * Multilevel Inheritance: Chain of inheritance (grandparent → parent → child).
* **`super()` function:** Used to call parent class methods inside child class.

---

### 2. Polymorphism

* **Definition:** Ability of different classes to be treated as instances of the same class through a common interface.
* **Types:**

  * **Method Overriding:** Child class redefines a method of the parent class.
  * **Method Overloading:** Same method name with different parameters (not natively supported in Python but can be mimicked).
* **Benefits:** Flexibility and dynamic method resolution at runtime.
* **Example:**

  ```python
  class Animal:
      def sound(self):
          print("Some sound")

  class Dog(Animal):
      def sound(self):
          print("Bark")

  class Cat(Animal):
      def sound(self):
          print("Meow")

  def make_sound(animal):
      animal.sound()

  make_sound(Dog())  # Bark
  make_sound(Cat())  # Meow
  ```

---

### 3. Operator Overloading

* **Definition:** Ability to define custom behavior for built-in operators (`+`, `-`, `*`, etc.) for user-defined classes.
* **Implemented by:** Defining special methods (dunder methods) like `__add__()`, `__sub__()`, etc.
* **Example:**

  ```python
  class Point:
      def __init__(self, x, y):
          self.x = x
          self.y = y

      def __add__(self, other):
          return Point(self.x + other.x, self.y + other.y)

      def __str__(self):
          return f"({self.x}, {self.y})"

  p1 = Point(1, 2)
  p2 = Point(3, 4)
  print(p1 + p2)  # (4, 6)
  ```
* **Common operator methods:**

  * `__add__(self, other)` → `+`
  * `__sub__(self, other)` → `-`
  * `__mul__(self, other)` → `*`
  * `__eq__(self, other)` → `==`
  * `__lt__(self, other)` → `<`

