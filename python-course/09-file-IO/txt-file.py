# Open for writing
f = open('example.txt', 'w')
f.write("Line A\nLine B\nLine C\n")
f.flush()  # Ensure it's written to disk
f.close()

# Reopen for reading
f = open('example.txt', 'r')
print("Read full:", f.read())
f.seek(0)
print("Readline:", f.readline().strip())
f.seek(0)
print("Readlines:", f.readlines())
f.close()

# Append
with open('example.txt', 'a') as f:
    f.write("Appended line\n")

# Write multiple lines using writelines
with open('example.txt', 'w') as f:
    f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

# Truncate file
with open('example.txt', 'r+') as f:
    f.truncate(12)  # Keep only first 12 bytes
    print("After truncate:", f.read())

# File info
with open('example.txt', 'r') as f:
    print("Tell:", f.tell())
    print("Isatty:", f.isatty())
    print("Fileno:", f.fileno())
