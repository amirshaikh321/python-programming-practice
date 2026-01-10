def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    is_long = len(password) >= 8
    
    if has_upper and has_digit and is_long:
        return "Strong Password"
    return "Weak Password: Needs 8+ chars, 1 uppercase, and 1 number."

print(check_password_strength("Python123"))  # Strong