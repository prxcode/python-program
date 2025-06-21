marks = {
    "John": 100,
    "Peter": 56,
    "Arthur": 23,
    0: "John"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"John": 99, "Renuka": 100})
# print(marks)

print(marks.get("John2")) # Prints None
print(marks["John2"]) # Returns an error