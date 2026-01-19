#type1 to import 


# import fib
# fib.fib()
# print(fib.a)



#type2 to import 

# from fib import fib,a
# fib()
# print(a)


#type 3  to import 


# from fib import * 
# fib()
# print(a)


# type 4 to import also we can do aliasing 

# import fib as a
# from fib import fib as f, a as b

# f()
# print(b)



# import sys
# print([i for i in sys.path])


# from package.sum import sum as add
# add(1,2)


# ** when using start we have to use all in init.py of nestedpackage init 

# from package.packages.nestedpackage import *

# print(abc())



# ** also you can add some path by using __path__ 
   # a) without package if you use __path__ in .py file it gives error
   #b) but inside __init__.py it will not give error 
   
import package
print(package.__path__)
package.__path__="/other/dict"
print(package.__path__)