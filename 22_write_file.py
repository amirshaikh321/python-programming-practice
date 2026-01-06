with open("demo.txt",'w') as file:
    file.write("this statement is written using python.")
with open("demo.csv",'w') as file:
        file.write('python')
     
    
with open("demo.txt",'r')as file:
    content = file.read()
    print(content)
with open("demo.csv",'r')as file:
    content = file.read()
    print(content)
