lst=[1,2,3,4,5]
import functools
newLst = functools.reduce(lambda ele1,ele2:ele1+ele2,lst)
print(newLst)