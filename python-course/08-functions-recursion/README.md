
### Chapter 8: Functions & Recursion

#### Defining and Calling Functions
Functions in Python are defined using the `def` keyword. They allow reuse of code, modularity, and cleaner logic.

```python
def greet():
    print("Hello")
greet()
````

#### Types of Function Arguments

Python supports several types of function arguments:

---

### 1. **Positional Arguments**

* Passed to functions in the same order as defined.
* Must match the number and order of parameters.

```python
def add(a, b):
    return a + b

add(3, 5)  # Output: 8
```

---

### 2. **Keyword Arguments**

* Arguments passed using parameter names.
* Order doesn't matter when using keywords.

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=25, name="Alice")
```

---

### 3. **Default Arguments**

* Provide default values for parameters.
* Used when you want to make a parameter optional.

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()         # Output: Hello, Guest
greet("Alice")  # Output: Hello, Alice
```

---

### 4. **Variable-length Arguments**

#### a. \*args (Non-keyword Variable-length Arguments)

* Collects extra positional arguments as a tuple.

```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4)  # Output: 10
```

#### b. \*\*kwargs (Keyword Variable-length Arguments)

* Collects extra keyword arguments as a dictionary.

```python
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# Output:
# name: Alice
# age: 25
```

---

### Recursion in Python

* A recursive function calls itself.
* Must have a **base case** to avoid infinite recursion.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

factorial(5)  # Output: 120
```
