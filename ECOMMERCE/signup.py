import hashlib
import uuid
import pwinput


def hash_password(password: str) -> str:
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password: str) -> bool:
    """Validate password complexity."""
    if len(password) < 8:
        print("Password length must be at least 8 characters")
        return False

    check_digit = False
    check_upper = False
    check_lower = False
    check_special = False

    for char in password:
        if char.islower():
            check_lower = True
        elif char.isupper():
            check_upper = True
        elif char.isdigit():
            check_digit = True
        elif char in "@$*&#":
            check_special = True

    if not check_digit:
        print("Password should contain at least one digit")
        return False
    if not check_upper:
        print("Password should contain at least one uppercase letter")
        return False
    if not check_lower:
        print("Password should contain at least one lowercase letter")
        return False
    if not check_special:
        print("Password should contain at least one special character")
        return False

    return True


def check_digit_in_name(name: str) -> bool:
    """Check if the name contains any digit."""
    return any(char.isdigit() for char in name)


def signup() -> dict:
    """Sign up a new user and return user data with hashed password."""
    # Name input
    name = input("Enter your name: ").strip()
    while len(name) < 3 or check_digit_in_name(name):
        print("Length of name should be at least 3 and contain no digits")
        name = input("Enter your name: ").strip()

    # Email input
    email = input("Enter your email: ").lower().strip()
    while '.com' not in email or '@' not in email or "gmail" not in email:
        if '.com' not in email:
            print("Email should include .com")
        if '@' not in email:
            print("Email should include @")
        email = input("Enter your email: ").lower().strip()

    # Password input with masking
    password = pwinput.pwinput(prompt="Enter your password: ").strip()
    while not check_password(password):
        password = pwinput.pwinput(prompt="Enter your password again: ").strip()

    # Hash the password
    hashed_password = hash_password(password)

    # Generate a unique user ID
    user_id = str(uuid.uuid4())

    return {
        "name": name,
        "email": email,
        "password": hashed_password,
        "id": user_id
    }
