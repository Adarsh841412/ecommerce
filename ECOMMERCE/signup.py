def check_password(password):
    if len(password)<8:
        print("password lengt must be greater than or equal to eight")
        return False
    
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

def check_digit(name):
    check_digits=False
    for i in name:
     if ord(i) >= 48 and ord(i) <= 57:
        return True

    return check_digits
def signup():
    
    name=input("enter your name:").strip()
  
    while(len(name)<3 or check_digit(name) ):
        print("length of name should be greater than 2 or not contain any digit")
        name=input("enter your name:").lower().strip()
    email=input("enter you email:").lower().strip()
    while('.com' not in email or'@' not in email or "gmail" not in email):
        if '.com ' not in email:
            print("email should be includ .com")
        if '@' not in email:
            print("email should include @")    
        email=input("enter your email:").lower().strip()

    # password 
    password=input("enter your password:").strip()
    
    while(True):
     check=check_password(password)
    
     if check==True:
        break
     else :
        password=input("Enter your password:").strip()   
    
    id=input("enter your id:").strip()
    while(id.isdigit()==False):
        print("id should contain only digits")
        id=input("enter your id:").strip()
    
    return {"name":name,"email":email,"password":password,"id":id}
