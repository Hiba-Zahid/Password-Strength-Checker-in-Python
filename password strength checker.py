import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error or lowercase_error or uppercase_error or digit_error or special_char_error:
        print("❌ Weak password. Issues:")
        if length_error:
            print("- Password must be at least 8 characters.")
        if lowercase_error:
            print("- Add at least one lowercase letter.")
        if uppercase_error:
            print("- Add at least one uppercase letter.")
        if digit_error:
            print("- Add at least one number.")
        if special_char_error:
            print("- Add at least one special character (!@#$ etc).")
    else:
        print("✅ Strong password!")

# Example usage
user_password = input("Enter your password to check strength: ")
check_password_strength(user_password)

