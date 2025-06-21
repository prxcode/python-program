
### Chapter 5: Dictionary & Sets

#### Properties of Dictionaries
- Dictionaries are unordered, mutable, and indexed collections.
- Defined using `{key: value}` pairs.
- Keys must be unique and immutable (e.g., strings, numbers, tuples).
- Values can be of any data type.
- Accessed via keys, not position.

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
````

#### Dictionary Methods

* `get(key[, default])`: Returns value or default.
* `keys()`, `values()`, `items()`: Returns view objects.
* `update(other_dict)`: Merges another dictionary.
* `pop(key[, default])`: Removes and returns value for key.
* `popitem()`: Removes and returns last key-value pair.
* `clear()`: Removes all items.
* `copy()`: Returns shallow copy.

```python
person.get("age")        # 25
person.update({"age": 26})
```

#### Sets in Python

* Sets are unordered, mutable collections of unique items.
* Defined using `{}` or `set()` function.
* No duplicate elements allowed.
* Cannot contain mutable items like lists.

```python
s = {1, 2, 3, 2}
print(s)  # Output: {1, 2, 3}
```

#### Properties and Operations on Sets

* Sets support mathematical operations:

  * `union()`, `intersection()`, `difference()`, `symmetric_difference()`
* Other methods:

  * `add()`, `remove()`, `discard()`, `pop()`, `clear()`, `copy()`
* Sets are unordered: no indexing or slicing.

```python
a = {1, 2, 3}
b = {3, 4, 5}
a.union(b)           # {1, 2, 3, 4, 5}
a.intersection(b)    # {3}
```
