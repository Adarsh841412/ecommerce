# f=open('file.txt','w')
# f.write("This is dog")
# f.write("\nThis is fish")
# f.close()

# f=open('file.txt','r')
# print(f.read())
# f.close()

# f=open('file.txt','a')
# f.write("\nThis is dhanveer's dog")
# f.close()

# f=open('file.txt','r')
# print(f.read())
# f.close()


# l=['\nAdarsh',"\nVishal"]
# f=open('file.txt','a')
# f.writelines(l)
# f.close()


# f=open('file.txt','r')
# print(f.read())
# f.close()


# ** read upto n characters

# f=open('file.txt','r')
# print(f.read(20))


# f=open('file.txt','r')
# while True:
#     data=f.readline()
#     print(data,end="")  
#     if data=="":
#         break
    
# with open('file.txt','r') as f:
#    f.read(20)
#    print(f.tell())
#    f.seek(0)
#    print(f.tell())


# *workign with binary files 

# with open('apple.avif','rb') as src:
#     data=src.read()
# with open('imag.jpeg','rb') as f:
#   with open('file.txt','w') as d:
#    d.write(f.read())




#    **********  working with other data types 

# with open('data.txt','w') as f:
#     f.write(5)


import json 

L=[1,2,3,4,5,]
# with open('data.txt','w') as f:
#   json.dump(L,f)

# with open('data.txt','r') as f:
#     print(f.read())



# L={"name":"adarsh","city":"chapra","age":12,"college":{"name":"adarshDubey"}}
# import json 
# with open('file.txt','r') as f:
#   d=json.load(f)
#   print(type(d))



# l=(1,2,3,4,5)
import pickle
# with open('file.txt','wb') as f:
#     p=pickle.dump(l,f)


# with open('file.txt','rb') as f:
#     p=pickle.load(f)
#     print(p)




#  namespace in python 

a=[1,1,3,4,5]
print(list(enumerate(a)))
