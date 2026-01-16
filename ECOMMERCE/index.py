from datetime import date

data_login_signup = int(input("Press 1 for login and 2 for signup:"))

user_data = []

def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_id = int(input("Enter your id: "))
    
    return {
        "name": name,
        "email": email,
        "password": password,
        "id": user_id
    }

def check_existing_user(user_data, email):
    for user in user_data:
        if user["email"] == email:
            return True
    return False

def login(user_data, email, password):
    for user in user_data:
        if user["email"] == email and user["password"] == password:
            return True
    return False



if data_login_signup == 2:
    count = int(input("How many users want to signup: "))

    while count > 0:
        new_user_data = register()
        email = new_user_data["email"]

        if check_existing_user(user_data, email):
            print("User already exists")
        else:
            user_data.append(new_user_data)
            print("Signup successful")
        count -= 1    

        

    print("All users:", user_data)


