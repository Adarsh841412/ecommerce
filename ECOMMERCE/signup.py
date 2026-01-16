def signup():
    name=input("enter your name:")
    email=input("enter you email:")
    password=input("enter your password:")
    id=int(input("enter your id:"))
    
    return {"name":name,"email":email,"password":password,"id":id}
