def resetPassword(user, user_data):
    data = input("Enter your correct email: ")

    if data == user["email"]:
        newPassword = input("Enter new password: ")
        user["password"] = newPassword

        for u in user_data:
            if u["email"] == user["email"]:
                u["password"] = newPassword
                print("Password reset successfully")
                return
        print("Your email not found in database")
    else:
        print("Incorrect email")
def login(user_data, email, password):
    for user in user_data:
        if user["email"] == email and user["password"] == password:
            return "success"

        elif user["email"] == email and user["password"] != password:
            choice = input("Press 1 to reset your password\n")
            if choice == '1':
                resetPassword(user, user_data)
                return "reset"
            return "fail"
    return "not_found"