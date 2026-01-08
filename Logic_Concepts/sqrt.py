def mySqrt(x: int):
    if x < 2:
        return x
    
    low, high = 2, x // 2
    ans = 1
    
    while low <= high:
        mid = (low + high) // 2
        num = mid * mid
        
        if num == x:
            return mid
        elif num < x:
            ans = mid  # Store mid as a potential answer
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
ans =mySqrt(4)
print(ans)