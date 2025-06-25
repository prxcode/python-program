# Chapter 12: Advanced Python 1

### 1. Newly Added Features in Python

* Python keeps evolving with new syntax and features to write cleaner, faster, and more readable code.
* Recent versions (3.8+) introduced several useful features enhancing code expressiveness and performance.

---

### 2. Walrus Operator (`:=`)

* Also called **assignment expression**.
* Allows assignment and return of a value within an expression.
* Syntax:

  ```python
  if (n := len(some_list)) > 5:
      print(f"List is too long ({n} elements)")
  ```
* Helps reduce code duplication by combining assignment and condition checks.

---

### 3. Advanced Type Hints

* Python supports **type hinting** to specify expected types for variables, function parameters, and return values.
* Helps with static type checking and better IDE support.
* Advanced hints include:

  * Union types (`Union[int, str]`)
  * Optional types (`Optional[str]` same as `Union[str, None]`)
  * Generics (`List[int]`, `Dict[str, float]`)
* Example:

  ```python
  from typing import List, Optional

  def greet(names: List[str]) -> None:
      for name in names:
          print(f"Hello, {name}")

  def find_user(id: int) -> Optional[str]:
      # Return string or None
      ...
  ```

---

### 4. Match Case (Structural Pattern Matching)

* Introduced in Python 3.10.
* Acts like a powerful `switch-case` statement.
* Matches values and structures, allowing elegant handling of complex branching.
* Example:

  ```python
  command = "start"
  match command:
      case "start":
          print("Starting")
      case "stop":
          print("Stopping")
      case _:
          print("Unknown command")
  ```

---

### 5. Dictionary Merge & Update Operators

* Python 3.9+ added new operators for dicts:

  * Merge (`|`): combines two dictionaries, returning a new one.
  * Update (`|=`): merges another dict into the original in-place.
* Example:

  ```python
  dict1 = {'a': 1, 'b': 2}
  dict2 = {'b': 3, 'c': 4}

  merged = dict1 | dict2       # {'a': 1, 'b': 3, 'c': 4}
  dict1 |= dict2               # dict1 updated to {'a': 1, 'b': 3, 'c': 4}
  ```

---

### 6. Exception Handling Enhancements

* `except` clauses now support multiple exceptions:

  ```python
  try:
      ...
  except (ValueError, TypeError) as e:
      print(f"Error: {e}")
  ```
* `finally` block ensures code runs regardless of exceptions.
* `else` block runs if no exception occurs.

---

### 7. Global Keyword and `enumerate()` Function

* **Global Keyword**: Used inside functions to modify a global variable.

  ```python
  count = 0

  def increment():
      global count
      count += 1
  ```
* **`enumerate()`**: Returns index and value while looping.

  ```python
  for index, value in enumerate(['a', 'b', 'c']):
      print(index, value)
  # Output: 0 a, 1 b, 2 c
  ```

---

### 8. List Comprehensions

* Concise way to create lists.
* Syntax:

  ```python
  [expression for item in iterable if condition]
  ```
* Example:

  ```python
  squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
  evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
  ```

