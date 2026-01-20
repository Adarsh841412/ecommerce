def check_password(password):
    checkdigit = False
    check_capital_alphabet = False
    check_small_alphabet = False
    check_special_characters = False

    for i in password:
    
        if ord(i) >= 97 and ord(i) <= 122:
            check_small_alphabet = True

  
        elif ord(i) >= 65 and ord(i) <= 90:
            check_capital_alphabet = True

    
        elif ord(i) >= 48 and ord(i) <= 57:
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


def reset_password(user, user_data):
    data = input("Enter your correct email: ").strip()

    if data == user["email"]:
        newPassword = input("Enter new password: ").strip()
        while(True):
           check_now= check_password(newPassword)
           if check_now==False:
            newPassword=input("Enter your password again:")
           if check_now==True:
            user["password"] = newPassword
            break


        for u in user_data:
            if u["email"] == user["email"]:
                u["password"] = newPassword
                print("Password reset successfully")
                print("re-enter you password and email")
                return True
        print("Your email not found in database")
    else:
        print("Incorrect email")
        return False
def login(user_data, email, password):
    for user in user_data:
        if user["email"] == email and user["password"] == password:
            return "success"
        elif user["email"]!=email:
            return "wrongemail"
        elif user["email"] == email and user["password"] != password:
            print("wrong password try again ")
            choice = input("Press1 for try agaoin\nPress 2 to reset your password\n")
            if choice=='1':
                return "tryagain"
            if choice=='2':
               check_now= reset_password(user, user_data)
               while check_now==False:
                reset_password(user,user_data)
                return "reset"    
            return "fail"
    return "not_found"
