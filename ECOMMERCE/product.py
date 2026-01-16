def add_products(user_id,user_data,user_product):
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


def view_products(user_detail,user_data,user_product):
    print("\n----------------------------------")
    print("YOUR PRODUCTS")
    print("----------------------------------")

    curr_user_products = filter(
        lambda data: data["id"] == user_detail["id"],
        user_product
    )

    print(list(curr_user_products))


def update_product(user_id,user_data,user_product):
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


def delete_product(user_id,user_data,user_product):
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
