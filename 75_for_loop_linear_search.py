number = [1,2,3,4,5]
for value in number: #Brings everything of the list in the in the variable called value
   print(value)#Unpacks all the digits of the list and prints.

l =[1,4,9,16,25,36,49,64,81,100]
for val in l:
   print(val)

t=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Number:"))#36
i=0
for value in t:
   if(x==value):
      print(f"The index is {i}")
   i+=1

# t = (1,4,9,16,25,36,49,64,81,1000)
# x=36
# i = 0
# while i<len(t):
#    if(t[i]==x):
#       print(f"found at index {i}")
#    i+=1
   