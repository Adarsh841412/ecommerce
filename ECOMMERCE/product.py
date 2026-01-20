from datetime import date
today=date.today()
today=today.strftime("%B %d, %Y")
def check_is_digit(data):
    if data.isdigit()==False:
        return False
    return True    
def add_products(user_id,curr_user_detail,user_product):
    print("\n----------------------------------")
    print("ADD PRODUCTS")
    print("----------------------------------")

    print("Logged in user:", curr_user_detail,)

    count_of_products = input("\nHow many products you want to add: ").strip()
     
    while(count_of_products.isdigit()==False):
        print("invalid input")
        count_of_products = input("\nHow many products you want to add: ").strip()
        while(not check_is_digit(count_of_products)):
            print("invalid input")
            count_of_products = input("\nHow many products you want to add: ").strip()
    count_of_products = int(count_of_products)

    while count_of_products > 0:
        print("\nEnter product details")
        print("----------------------")
        name = input("Product name     : ").strip()
        while(name.isalpha()==False):
            print("name should only contain alphabet")
            name = input("Product name     : ").strip()

        price = input("Product price    : ").strip()
        while(not check_is_digit(price)):
            print("invalid input, it must be integer")
            price = input("Product price    : ").strip()
        quantity = input("Product quantity : ").strip()
        while(not check_is_digit(quantity)):
             print("invalid input, it must be integer")
             quantity = input("Product quantity : ").strip()
        buying_date = today

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


def view_products(user_detail,user_product):
    print("\n----------------------------------")
    print("YOUR PRODUCTS")
    print("----------------------------------")

    curr_user_products = filter(
        lambda data: data["id"] == user_detail["id"],
        user_product
    )

    print(list(curr_user_products))


def update_product(user_id,curr_user_detail,user_product):
    print("\n----------------------------------")
    print("UPDATE PRODUCT")
    print("----------------------------------")

    name_of_product = input("Enter product name to update: ").strip()


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


def delete_product(user_id,curr_user_detail,user_product):
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
