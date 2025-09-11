def is_valid(password):
    if len(password) < 8:
        return False
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)
    return has_upper and has_digit and has_special

# Test
print(is_valid("Pass123!"))  # True
print(is_valid("pass123"))   # False
