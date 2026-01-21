import hashlib
import pwinput


def hash_password(password: str) -> str:
    """Return SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(input_password: str, stored_hash: str) -> bool:
    """Check if the input password matches the stored hashed password."""
    return hash_password(input_password) == stored_hash


def check_password(password: str) -> bool:
    """Validate password complexity rules."""
    checkdigit = False
    check_capital_alphabet = False
    check_small_alphabet = False
    check_special_characters = False

    for i in password:
        if 'a' <= i <= 'z':
            check_small_alphabet = True
        elif 'A' <= i <= 'Z':
            check_capital_alphabet = True
        elif '0' <= i <= '9':
            checkdigit = True
        elif i in "@$*&#":
            check_special_characters = True

    if not checkdigit:
        print("Password should contain at least one digit")
        return False
    if not check_capital_alphabet:
        print("Password should contain at least one uppercase letter")
        return False
    if not check_small_alphabet:
        print("Password should contain at least one lowercase letter")
        return False
    if not check_special_characters:
        print("Password should contain at least one special character")
        return False

    return True


def reset_password(user: dict, user_data: list) -> bool:
    """Reset the password for the given user."""
    data = input("Enter your correct email: ").strip()

    if data != user["email"]:
        print("Incorrect email")
        return False

    new_password = pwinput.pwinput(prompt="Enter your new password: ")

    while not check_password(new_password):
        new_password = pwinput.pwinput(prompt="Enter your new password again: ")

    hashed_new_password = hash_password(new_password)

    for u in user_data:
        if u["email"] == user["email"]:
            u["password"] = hashed_new_password
            print("Password reset successfully")
            print("Re-enter your email and password")
            return True

    print("Your email not found in database")
    return False


def login(user_data: list, email: str, password: str) -> str:
    """Login function using hashed passwords."""
    for user in user_data:

        if user["email"] == email and verify_password(password, user["password"]):
            return "success"

        elif user["email"] == email and not verify_password(password, user["password"]):
            print("Wrong password, try again")
            choice = input(
                "Press 1 to try again\n"
                "Press 2 to reset your password\n"
            ).strip()

            if choice == '1':
                return "tryagain"
            elif choice == '2':
                check_now = reset_password(user, user_data)
                if check_now:
                    return "reset"
                else:
                    return "fail"
            return "fail"

    return "not_found"
