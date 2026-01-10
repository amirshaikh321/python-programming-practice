def perfect_num(num):

    if num<1:
        print("invalid number")
    
    divisor_sum=0
    for i in range(1,num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print("it is perfect number")
    else:
        print("it is not perfect number")
perfect_num(6)
