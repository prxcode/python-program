
### Chapter 6: Conditional Expression

#### if, else, and elif statements

* Control the flow based on conditions.
* `if`: Executes block if condition is `True`.
* `elif`: Checks another condition if previous `if`/`elif` was `False`.
* `else`: Executes if all above conditions are `False`.

```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

#### Relational and Logical Operators

* **Relational Operators**:

  * `==`, `!=`, `>`, `<`, `>=`, `<=`
* **Logical Operators**:

  * `and`: True if both are true
  * `or`: True if at least one is true
  * `not`: Negates the condition

```python
x = 5
if x > 0 and x < 10:
    print("x is between 1 and 9")
```
