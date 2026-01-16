from datetime import date
import sys
import os
user_data = []
user_product = []

print("\n==================================================")
print("        USER PRODUCT MANAGEMENT SYSTEM")
print("==================================================\n")

data_login_signup = int(input(
    f"1. Signup ({len(user_data)} users)\n"
    f"2. Exit\n"
    f"----------------------------------\n"
    f"Enter choice: "
))

if data_login_signup == 2:
    print("Restarting program...")
    os.execv(sys.executable, ['python'] + sys.argv)

from signup import signup
from login import login
from product import add_products,view_products,update_product,delete_product

def check_existing_user(user_data, email):
    for user in user_data:
        if user["email"] == email:
            return True
    return False


def add_products(user_id):
    print("\n----------------------------------")
    print("ADD PRODUCTS")
    print("----------------------------------")

    print("Logged in user:", curr_user_detail)

    count_of_products = int(input("\nHow many products you want to add: "))

    while count_of_products > 0:
        print("\nEnter product details")
        print("----------------------")
        name = input("Product name     : ")
        price = int(input("Product price    : "))
        quantity = int(input("Product quantity : "))
        buying_date = date.today()

        user_product.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "buying_date": buying_date,
            "id": user_id
        })

        print("\nProduct added successfully")
        print(user_product)

        count_of_products -= 1


def view_products(user_detail):
    print("\n----------------------------------")
    print("YOUR PRODUCTS")
    print("----------------------------------")

    curr_user_products = filter(
        lambda data: data["id"] == user_detail["id"],
        user_product
    )

    print(list(curr_user_products))


def update_product(user_id):
    print("\n----------------------------------")
    print("UPDATE PRODUCT")
    print("----------------------------------")

    name_of_product = input("Enter product name to update: ")

    matched_products = list(
        filter(
            lambda data: data["name"] == name_of_product and data["id"] == user_id,
            user_product
        )
    )

    if not matched_products:
        print("Product not found")
        return

    product = matched_products[0]

    print("\nCurrent product details")
    print("-----------------------")
    print(product)

    new_name = input("\nNew name (Enter to skip)     : ")
    new_price = input("New price (Enter to skip)    : ")
    new_quantity = input("New quantity (Enter to skip): ")

    if new_name:
        product["name"] = new_name
    if new_price:
        product["price"] = int(new_price)
    if new_quantity:
        product["quantity"] = int(new_quantity)

    print("\nProduct updated successfully")
    print(user_product)


def delete_product(user_id):
    print("\n----------------------------------")
    print("DELETE PRODUCT")
    print("----------------------------------")

    name_of_product = input("Enter product name to delete: ")

    for product in user_product:
        if product["id"] == user_id and product["name"] == name_of_product:
            user_product.remove(product)
            print("\nProduct deleted successfully")
            return

    print("\nProduct not found")


if data_login_signup == 1:
    print("\n----------------------------------")
    print("USER SIGNUP")
    print("----------------------------------")

    count = int(input("How many users want to signup: "))

    while count > 0:
        new_user_data = signup()
        email = new_user_data["email"]

        if check_existing_user(user_data, email):
            print("User already exists")
        else:
            user_data.append(new_user_data)
            print("Signup successful")

        count -= 1

    data_login_signup = int(input(
        "\n1. Login\n"
        "2. Exit\n"
        "-----------------\n"
        "Enter choice: "
    ))

    if data_login_signup == 2:
        print("\nProgram ended.\n")
        sys.exit()



if data_login_signup == 1:
    print("\n----------------------------------")
    print("USER LOGIN")
    print("----------------------------------")

    while True:
        email = input("Email    : ")
        password = input("Password : ")

        if login(user_data, email, password):
            print("\nLogin successful")
            break
        else:
            print("Wrong user details")

    curr_user_detail = next(user for user in user_data if user["email"] == email)

    while True:
        print("\n==================================")
        print("DASHBOARD MENU")
        print("==================================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")

        choice = int(input("\nEnter choice: "))

        match choice:
            case 1:
                add_products(curr_user_detail["id"])
            case 2:
                view_products(curr_user_detail)
            case 3:
                update_product(curr_user_detail["id"])
            case 4:
                delete_product(curr_user_detail["id"])
            case _:
                print("Invalid choice")

        cont = input("\nContinue? (yes/no): ").lower()
        if cont != "yes":
            print("\nThank you. Program finished.\n")
            break
