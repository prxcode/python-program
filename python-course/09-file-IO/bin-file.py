# Write binary data
with open('example.bin', 'wb') as f:
    f.write(bytes([0, 1, 2, 3, 255]))
    f.flush()

# Read binary data
with open('example.bin', 'rb') as f:
    print("Binary Read:", f.read())

# Append binary data
with open('example.bin', 'ab') as f:
    f.write(bytes([10, 20]))

# Seek and tell in binary
with open('example.bin', 'rb') as f:
    f.seek(2)
    print("Seek to 2 and read 3 bytes:", f.read(3))
    print("File pointer at:", f.tell())
