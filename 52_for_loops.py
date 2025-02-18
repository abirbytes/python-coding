#A for loop is used to iterate through a sequence like list,tuple, or string[]
for i in range (4): #0 to 3 (0,4)
   print(i)

for j in range (0,10,2):
   print(j)
#For loops in lists

l= [1,4,6,234,6,764]
for p in l:
   print(p)

#For loops in tuples
t= (6,231,75,122)
for k in t:
   print(k)
   
#For loop in strings
strs= "Harry"
for h in strs:
   print(h)

#For loop with else
l2=[1,7,9,5,6,10]
for item in l2:
   print(item)
else:
   print("done")#Prints the else when loop exhausts or nothing left in the loop