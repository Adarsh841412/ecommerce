from datetime import date

TODAY = date.today().strftime("%B %d, %Y")


def check_is_digit(data: str) -> bool:
    """Check if the given data is a digit."""
    return data.isdigit()


def add_products(user_id: str, curr_user_detail: dict, user_product: list):
    print("\n----------------------------------")
    print("ADD PRODUCTS")
    print("----------------------------------")
    print("Logged in user:", curr_user_detail)

    count_of_products = input("\nHow many products you want to add: ").strip()

    while not check_is_digit(count_of_products):
        print("Invalid input. Enter a number.")
        count_of_products = input("\nHow many products you want to add: ").strip()

    count_of_products = int(count_of_products)

    while count_of_products > 0:
        print("\nEnter product details")
        print("----------------------")

        name = input("Product name     : ").strip()
        while not name.isalpha():
            print("Name should only contain alphabets")
            name = input("Product name     : ").strip()

        price = input("Product price    : ").strip()
        while not check_is_digit(price):
            print("Invalid input, it must be an integer")
            price = input("Product price    : ").strip()

        quantity = input("Product quantity : ").strip()
        while not check_is_digit(quantity):
            print("Invalid input, it must be an integer")
            quantity = input("Product quantity : ").strip()

        buying_date = TODAY

        user_product.append({
            "name": name,
            "price": int(price),
            "quantity": int(quantity),
            "buying_date": buying_date,
            "id": user_id
        })

        print("\nProduct added successfully")
        count_of_products -= 1


def view_products(user_detail: dict, user_product: list):
    print("\n----------------------------------")
    print("YOUR PRODUCTS")
    print("----------------------------------")
    print("Logged in user:", user_detail)
    print()
    curr_user_products = list(
        filter(lambda data: data["id"] == user_detail["id"], user_product)
    )

    if not curr_user_products:
        print("No products found.")
        return

    for idx, product in enumerate(curr_user_products, start=1):
        print(f"{idx}. Name: {product['name']}, Price: {product['price']}, "
              f"Quantity: {product['quantity']}, Buying Date: {product['buying_date']}")


def update_product(user_id: str, curr_user_detail: dict, user_product: list):
    print("\n----------------------------------")
    print("UPDATE PRODUCT")
    print("----------------------------------")

    name_of_product = input("Enter product name to update: ").strip()

    matched_products = [
        p for p in user_product if p["name"] == name_of_product and p["id"] == user_id
    ]

    if not matched_products:
        print("Product not found")
        return

    product = matched_products[0]
    print("\nCurrent product details")
    print("-----------------------")
    print(product)

    new_name = input("New name (Enter to skip)     : ").strip()
    new_price = input("New price (Enter to skip)    : ").strip()
    new_quantity = input("New quantity (Enter to skip) : ").strip()

    if new_name:
        product["name"] = new_name
    if new_price and check_is_digit(new_price):
        product["price"] = int(new_price)
    if new_quantity and check_is_digit(new_quantity):
        product["quantity"] = int(new_quantity)

    print("\nProduct updated successfully")


def delete_product(user_id: str, curr_user_detail: dict, user_product: list):
    print("\n----------------------------------")
    print("DELETE PRODUCT")
    print("----------------------------------")

    name_of_product = input("Enter product name to delete: ").strip()

    for product in user_product:
        if product["id"] == user_id and product["name"] == name_of_product:
            user_product.remove(product)
            print("\nProduct deleted successfully")
            return

    print("\nProduct not found")
