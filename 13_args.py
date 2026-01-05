# non keyword arguments

def func(*args):
    list = []
    list.append(args)
    return list
print(func(1,2,3))
