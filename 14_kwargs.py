# keyword arguments

def any(**kwargs):
    for key,val in kwargs.items():
        print(key,"=", val)


any(name= "alice",age=15)