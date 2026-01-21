from datetime import date
import sys
import os
from Data import user_data, user_product
from signup import signup
from login import login
from product import add_products, view_products, update_product, delete_product
import pwinput
print("\n==================================================")
print("        USER PRODUCT MANAGEMENT SYSTEM")
print("==================================================\n")

data_login_signup = input(
    f"1. Signup ({len(user_data)} users)\n"
    f"2. Restart\n"
    f"3. Exit\n"
    f"4. Login\n"
    f"----------------------------------\n"
    f"Enter choice: "
)

while not data_login_signup.isdigit() or int(data_login_signup) > 4:
    print("Inappropriate selection, try again.")
    data_login_signup = input(
        f"1. Signup ({len(user_data)} users)\n"
        f"2. Restart\n"
        f"3. Exit\n"
        f"4. Login\n"
        f"----------------------------------\n"
        f"Enter choice: "
    )

if data_login_signup == '3':
    print("Program is exiting.")
    sys.exit()

if data_login_signup == '2':
    print("Restarting program...")
    os.execv(sys.executable, ['python'] + sys.argv)


def check_existing_user(user_data, email):
    for user in user_data:
        if user["email"] == email:
            return True
    return False


def signup_condition():
    print("\n----------------------------------")
    print("USER SIGNUP")
    print("----------------------------------")

    while True:
        new_user_data = signup()
        email = new_user_data["email"]

        if check_existing_user(user_data, email):
            print("User already exists")
            continue
        else:
            user_data.append(new_user_data)
            print("Signup successful")
            break

    data_login_signup_local = input(
        "\n4. Login\n"
        "2. Exit\n"
        "-----------------\n"
        "Enter choice: "
    )

    while not data_login_signup_local.isdigit() or int(data_login_signup_local) not in (2, 4):
        print("Invalid input")
        data_login_signup_local = input(
            "\n4. Login\n"
            "2. Exit\n"
            "-----------------\n"
            "Enter choice: "
        )

    if data_login_signup_local == '2':
        print("\nProgram ended.\n")
        sys.exit()
    return


if data_login_signup == '1':
    signup_condition()


def login_user():
    print("\n----------------------------------")
    print("USER LOGIN")
    print("----------------------------------")

    while True:
        email = input("Email    : ").strip()
        password = pwinput.pwinput(prompt="password: ")


        result = login(user_data, email, password)

        if result == "success":
            print("\nLogin successful")
            break
        elif result == "not_found":
            print("User does not exist:")
            choice = input("Enter 1 for signup \nEnter 2 to try again: ")
            if choice == '1':
                signup_condition()
                continue
        elif result == "tryagain":
            continue
        elif result == "reset":
            continue

    curr_user_detail = next(user for user in user_data if user["email"] == email)

    while True:
        print("\n==================================")
        print("DASHBOARD MENU")
        print("==================================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Logout")

        choice = input("\nEnter choice: ").strip()

        match choice:
            case '1':
                add_products(curr_user_detail["id"], curr_user_detail, user_product)
            case '2':
                view_products(curr_user_detail, user_product)
            case '3':
                update_product(curr_user_detail["id"], curr_user_detail, user_product)
            case '4':
                delete_product(curr_user_detail["id"], curr_user_detail, user_product)
            case '5':
                print("\nLogged out successfully.\n")
                while True:
                    choice_logout = input(
                        "Enter 1 for signup\n"
                        "Enter 2 for login\n"
                        "-----------------\n"
                        "Enter choice: "
                    ).strip()
                    if choice_logout == '1':
                        signup_condition()
                        break
                    elif choice_logout == '2':
                        break
                    else:
                        print("Invalid input. Please enter 1 or 2.")
                break
            case _:
                print("Invalid choice")

        cont = input("\nContinue? (yes/no): ").lower()
        while "yes" not in cont and "no" not in cont:
            print("Invalid input")
            cont = input("\nContinue? (yes/no): ").lower()

        if cont != "yes":
            print("\nThank you. Program finished.\n")
            break


if data_login_signup in ('1', '4'):
    while True:
        login_user()

        while True:
            choice_relogin = input(
                "\nEnter 1 for re-login\n"
                "Enter 2 for exit\n"
                "------------------\n"
                "Enter choice: "
            ).strip()

            if choice_relogin == '1':
                break
            elif choice_relogin == '2':
                print("Program exited.")
                sys.exit()
            else:
                print("Invalid input. Please enter 1 or 2.")
