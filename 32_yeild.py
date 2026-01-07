def count_to_three():
    yield 1
    yield 2
    yield 3

counter = count_to_three()
print(next(counter))
print(next(counter))