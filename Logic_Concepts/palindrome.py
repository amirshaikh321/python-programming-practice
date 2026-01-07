def is_palindrome(data):
    clean_data = str(data).lower()

    return clean_data == clean_data[::-1]

print(is_palindrome("Racecar"))
print(is_palindrome(121))