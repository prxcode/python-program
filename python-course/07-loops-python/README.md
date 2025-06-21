### Chapter 7: Loops in Python

#### while loop

* Repeats a block while a condition is `True`.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

#### for loop

* Iterates over iterable objects (lists, strings, etc.).

```python
for i in [1, 2, 3]:
    print(i)
```

#### range() function

* Generates a sequence of numbers.
* `range(start, stop, step)`

```python
for i in range(1, 6, 2):  # 1, 3, 5
    print(i)
```

#### for loop with else

* `else` executes after loop completes (if not broken).

```python
for i in range(3):
    print(i)
else:
    print("Loop finished")
```

#### Break, continue, and pass statements

* `break`: Exits loop immediately.
* `continue`: Skips to next iteration.
* `pass`: Does nothing (placeholder).

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

