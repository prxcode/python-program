# Chapter 3: Strings

---

## 1. String Slicing

A **string** is a sequence of characters.

```python
text = "Python"
print(text[0])    # Output: P
print(text[1:4])  # Output: yth
print(text[:3])   # Output: Pyt
print(text[2:])   # Output: thon
print(text[-1])   # Output: n
```

* `string[start:end]` includes `start` but excludes `end`
* Indexing starts at `0`; negative indexes count from the end

---

## 2. Slicing with Skip Values

Skip characters while slicing using a **step value**:

```python
text = "PythonProgramming"
print(text[::2])   # Output: PtoPormig
print(text[1::3])  # Output: yhrgmg
```

* Syntax: `string[start:end:step]`
* Useful for patterns, encryption, or reversing strings:
```python
print(text[::-1])  # Output: reversed string
```

---

## 3. String Functions (Methods)

Python provides built-in methods for string manipulation:

| Method             | Description                          | Example                        |
|--------------------|--------------------------------------|--------------------------------|
| `len()`            | Length of the string                 | `len("hello")` → `5`           |
| `lower()`          | Converts to lowercase                | `"Hi".lower()` → `"hi"`        |
| `upper()`          | Converts to uppercase                | `"hi".upper()` → `"HI"`        |
| `strip()`          | Removes leading/trailing spaces      | `" hello ".strip()` → `"hello"`|
| `replace(old, new)`| Replaces substring                   | `"apple".replace("a", "A")`    |
| `find(sub)`        | Finds index of first occurrence      | `"hello".find("e")` → `1`      |

---

## 4. Escape Sequence Characters

Used to insert special characters inside strings:

| Escape | Meaning             | Example Output           |
|--------|---------------------|--------------------------|
| `\n`   | New line            | `"Hello\nWorld"`         |
| `\t`   | Tab space           | `"Hello\tWorld"`         |
| `\\`   | Backslash (`\`)     | `"C:\\Path\\file.txt"`   |
| `\'`   | Single quote        | `'It\'s fine'`           |
| `\"`   | Double quote        | `"He said, \"Hi\""`      |

Escape sequences begin with a backslash (`\`) and tell Python to treat the next character specially.

---
