# Chapter 13: Advanced Python 2

### 1. Virtual Environments

* **Purpose:** Isolate project-specific Python packages and dependencies.
* Avoids conflicts between projects.
* Create a virtual environment:

  ```bash
  python -m venv env_name
  ```
* Activate:

  * Windows: `.\env_name\Scripts\activate`
  * macOS/Linux: `source env_name/bin/activate`
* Deactivate:

  ```bash
  deactivate
  ```

---

### 2. Lambda Functions

* Anonymous, inline functions without a name.
* Syntax:

  ```python
  lambda arguments: expression
  ```
* Useful for short functions passed as arguments.
* Example:

  ```python
  add = lambda x, y: x + y
  print(add(3, 4))  # Output: 7
  ```

---

### 3. String Methods: `join()` and `format()`

* **`join()`**

  * Joins elements of an iterable (like list) into a single string with a separator.
  * Example:

    ```python
    words = ['Hello', 'World']
    sentence = ' '.join(words)  # "Hello World"
    ```

* **`format()`**

  * Formats strings by replacing placeholders `{}` with variables.
  * Example:

    ```python
    name = "Alice"
    age = 30
    text = "My name is {} and I am {} years old.".format(name, age)
    ```

---

### 4. Functional Programming: `map()`, `filter()`, and `reduce()`

* **`map(function, iterable)`**
  Applies a function to all items in an iterable and returns an iterator.

  ```python
  nums = [1, 2, 3]
  squares = map(lambda x: x**2, nums)  # squares: 1, 4, 9
  print(list(squares))
  ```

* **`filter(function, iterable)`**
  Filters items out of iterable for which function returns `True`.

  ```python
  nums = [1, 2, 3, 4, 5]
  evens = filter(lambda x: x % 2 == 0, nums)  # evens: 2, 4
  print(list(evens))
  ```

* **`reduce(function, iterable)`**
  Applies a rolling computation to sequential pairs in iterable (import from `functools`).

  ```python
  from functools import reduce
  nums = [1, 2, 3, 4]
  product = reduce(lambda x, y: x * y, nums)  # 24
  print(product)
  ```

