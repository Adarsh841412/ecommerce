def login(user_data,email,password):

    for user in user_data:
        if user["email"] == email and user["password"]==password:
            return True
        else:
             return False
