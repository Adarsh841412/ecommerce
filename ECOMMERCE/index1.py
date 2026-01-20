from datetime import date
import sys
import os

user_data = []
user_product = []

print("\n==================================================")
print("        USER PRODUCT MANAGEMENT SYSTEM")
print("==================================================\n")

data_login_signup = input(
    f"1. Signup ({len(user_data)} users)\n"
    f"2. Restart\n"
     f"3. Exit\n"
    f"----------------------------------\n"
    f"Enter choice: "
)

while(data_login_signup.isdigit()==False or int(data_login_signup)>3):
  print("inappropirate selection ,Try again")
  data_login_signup = input(
    f"1. Signup ({len(user_data)} users)\n"
    f"2. Restart\n"
    f"3. Exit\n"
    f"----------------------------------\n"
    f"Enter choice: "
)

if data_login_signup=='3':
    print("program is exit")
    sys.exit()


if data_login_signup == '2':
    print("Restarting program...")
    os.execv(sys.executable, ['python'] + sys.argv)

from signup import signup
from login import login
from product import add_products, view_products, update_product, delete_product


def check_existing_user(user_data, email):
    for user in user_data:
        if user["email"] == email:
            return True
    return False


if data_login_signup == '1':
    print("\n----------------------------------")
    print("USER SIGNUP")
    print("----------------------------------")

    while(True):
        new_user_data = signup()
        email = new_user_data["email"]

        if check_existing_user(user_data, email):
            print("User already exists")
            continue
        else:
            user_data.append(new_user_data)
            print("Signup successful")
            break


    data_login_signup = input(
        "\n1. Login\n"
        "2. Exit\n"
        "-----------------\n"
        "Enter choice: "
    )
    while(not data_login_signup.isdigit() or int(data_login_signup)>2):
        print("invalid input")
        data_login_signup = input(
        "\n1. Login\n"
        "2. Exit\n"
        "-----------------\n"
        "Enter choice: ")
                   
   
    if data_login_signup == '2':
        print("\nProgram ended.\n")
        sys.exit()


if data_login_signup =='1':
    print("\n----------------------------------")
    print("USER LOGIN")
    print("----------------------------------")

    while True:
        email = input("Email    : ").strip()
        password = input("Password : ").strip()

        result = login(user_data, email, password)

        if result == "success":
            print("\nLogin successful")
            break
        elif result=="wrongemail":
            print("you entered wrong email,Try again") 
            continue   
        elif result == "tryagain":
            continue
        elif result=="reset":
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
            case _:
                print("Invalid choice")

        cont = input("\nContinue? (yes/no): ").lower()
        while("yes"  not in cont and 'no' not in cont):
            print("invalid input")
            cont = input("\nContinue? (yes/no): ").lower()
            if cont=="yes" or cont=="no":
                break

        if cont != "yes":
            print("\nThank you. Program finished.\n")
            break
