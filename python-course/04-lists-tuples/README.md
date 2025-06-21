
# Chapter 4: Lists and Tuples

## List Indexing

- Lists are ordered collections of items, defined using square brackets `[]`.
- Indexing starts at 0. Negative indexing starts from the end (`-1` refers to the last item).
- Syntax: `list[index]`
  ```python
  fruits = ['apple', 'banana', 'cherry']
  print(fruits[0])    # 'apple'
  print(fruits[-1])   # 'cherry'


* Slicing: Extracts a sublist using `[start:stop:step]`

  ```python
  fruits[1:3]  # ['banana', 'cherry']
  fruits[:2]   # ['apple', 'banana']
  ```

## List Methods

Commonly used list methods:

* `append(x)`: Adds item `x` to the end.
* `extend(iterable)`: Adds elements from an iterable.
* `insert(i, x)`: Inserts `x` at index `i`.
* `remove(x)`: Removes first occurrence of `x`.
* `pop([i])`: Removes and returns item at index `i` (last if `i` not given).
* `clear()`: Removes all items.
* `index(x)`: Returns first index of `x`.
* `count(x)`: Counts how many times `x` occurs.
* `sort()`: Sorts the list in-place.
* `reverse()`: Reverses the list in-place.
* `copy()`: Returns a shallow copy of the list.

```python
numbers = [3, 1, 4]
numbers.append(5)    # [3, 1, 4, 5]
numbers.sort()       # [1, 3, 4, 5]
```

## Tuples in Python

* Tuples are immutable sequences, defined with parentheses `()`.
* Can store heterogeneous data types.
* Useful for fixed data collections and as dictionary keys.

```python
t = (1, 2, 3)
single = (1,)   # Single-element tuple requires comma
```

* Supports indexing and slicing like lists.
* Cannot modify, append, or remove elements.

## Tuple Methods

Only two built-in methods:

* `count(x)`: Returns the number of times `x` appears.
* `index(x)`: Returns the first index of `x`.

```python
t = (1, 2, 2, 3)
t.count(2)   # 2
t.index(3)   # 3
```

> **Note**: Tuples are faster and safer than lists for fixed-size, read-only collections.

```

Let me know if you'd like it saved as a file or want additional examples or diagrams.
```
