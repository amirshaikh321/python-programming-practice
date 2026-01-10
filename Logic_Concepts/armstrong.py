def armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    total_sum = 0
    for digit in num_str:
        total_sum += int(digit)** num_len
    
    if total_sum == number:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

armstrong(153)