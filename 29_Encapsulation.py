
class school:
    def result(self):
        self.subject = "maths" #Public (accessible everywhere)
        self.__marks = 97 # private (Only accessible inside the class)
        
        return self.subject, self.__marks

s1 = school()
print(s1.result())