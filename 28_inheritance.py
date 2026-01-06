class car():
    def color(self, color):
        print(f'Color of car is {color}')

class SUV(car):

    def model(self, model_name):
        print(f"Model of the SUV is {model_name}")

car1 = SUV()
car1.model("mercedez benz")
car1.color('red')