
class animal:
    def __init__(self):
        print("this is a animal")

class dog(animal):
    def speak(self):
        print("Bark")
class cat(animal):
    def speak(self):
        print("Meaw")

c1 = cat()
c1.speak()
d1 =dog()
d1.speak()