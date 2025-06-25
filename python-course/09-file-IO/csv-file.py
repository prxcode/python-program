import csv

# Write CSV
with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerows([['Alice', '30'], ['Bob', '25']])

# Read CSV using csv.reader
with open('example.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV row:", row)

# Append a row
with open('example.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Charlie', '22'])
