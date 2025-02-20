#Print numbers from 1 to 100
number1=1
while number1<=100:
   print(number1)
   number1 +=1

#Print number 100 to 1
number2 = 100
while number2 >=1:
   print(number2)
   number2 -=1

#Print the multiplication table of a number n
# n = int(input("Enter the number:"))
# m = 1
# while m<=10:
#    print(f"{n} x {m} = {n*m}")
#    m+=1

#Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
l=[1,4,9,16,25,36,49,64,81,100]
i = 0
while i < 10:
   print(l[i])
   i+=1

#Search for a number x in this tuple using loop
t = (1,4,9,16,25,36,49,64,81,1000)
x=36
i = 0
while i<len(t):
   if(t[i]==x):
      print(f"found at index {i}")
   i+=1
   