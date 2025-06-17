# Chapter 2: Variables and Data Types

---

## 1. Defining Variables

A **variable** is a name used to store data.

```python
x = 10
name = "Alice"
```

* Variables don't need explicit declaration or data types.
* The value assigned determines the type.

---

## 2. Data Types in Python

Common built-in data types:

| Type       | Example           |
|------------|-------------------|
| `int`      | `5`, `-3`, `100`  |
| `float`    | `3.14`, `-0.5`    |
| `str`      | `"hello"`, `'A'`  |
| `bool`     | `True`, `False`   |
| `list`     | `[1, 2, 3]`       |
| `tuple`    | `(4, 5)`          |
| `dict`     | `{"a": 1, "b": 2}`|

---

## 3. Rules for Choosing an Identifier

Identifiers are names for variables, functions, etc.

✅ Valid rules:
- Must start with a letter or underscore (`_`)
- Can contain letters, digits, underscores
- Case-sensitive (`name` ≠ `Name`)

❌ Invalid examples:
```python
1name = "wrong"     # Cannot start with a digit
my-name = "wrong"   # Hyphen not allowed
```

---

## 4. Operators in Python

Operators perform operations on variables.

| Type            | Operators               | Example        |
|-----------------|-------------------------|----------------|
| Arithmetic      | `+`, `-`, `*`, `/`, `**`, `//`, `%` | `x + y` |
| Assignment      | `=`, `+=`, `-=`, `*=`, `/=` | `x += 1`     |
| Comparison      | `==`, `!=`, `>`, `<`, `>=`, `<=` | `x == y` |
| Logical         | `and`, `or`, `not`       | `x and y`     |

---

## 5. `type()` Function & Typecasting

### `type()` – Check variable type:

```python
x = 10
print(type(x))  # <class 'int'>
```

### Typecasting – Convert one type to another:

```python
x = "5"
y = int(x)  # Converts string to integer
```

Common casting functions: `int()`, `float()`, `str()`, `bool()`

---

## 6. `input()` Function

Used to take user input:

```python
name = input("Enter your name: ")
print("Hello", name)
```

* Input is always received as a `str`. Use typecasting to convert.

```python
age = int(input("Enter your age: "))
```

---
