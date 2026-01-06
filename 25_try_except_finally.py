try:
    num1= int(input('Enter a number:'))
    num2= int(input('Enter a number:'))
    reulst = num1/num2

except ZeroDivisionError:
    print("Error: You cannot divide by zero")

except ValueError:
    print("Error: Invalid number")
finally:
    print("always runs finally code")