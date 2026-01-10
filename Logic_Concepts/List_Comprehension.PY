names = ["Alice", "Bob", "Amanda", "Charlie", "Alex"]
a_names = []
for name in names:
    if name.startswith('A'):
        a_names.append(name.upper())

print(a_names)