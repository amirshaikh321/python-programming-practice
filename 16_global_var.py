
list = []

def func():
    global list
    for i in range(1,10):
        list.append(i)

func()
print(list)