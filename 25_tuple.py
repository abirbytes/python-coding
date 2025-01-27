a=(1,)#One element tuple. if we dont use the comma after 1 python will take it as an integer
print(type(a))
b=()#Empty Tuple
print(type(b))
c=(1,78.88,55,False,"Abir","LAm")
#we can't make changes in tuple directly like lists
print(c.count(78.88))
print(c.index(55))#Index of the value in the tuple
print(c*2)#writes the tuple two times
print(55 in c)#Prints true if the value is presented in the tuple....
print(len(c))#To print the length of the tuple
print(c[0:2])#slices the tuple
e,f,g,h,i,j= c
print(e,f,g,h,i,j)#stores the tuples into variables by unpacking it
print(e*2)