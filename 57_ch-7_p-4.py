n = int(input("enter the number:"))
for i in range(2,n):
   if(n%i)==0:
      print("Number is not a prime number")
      break
   else:
      print("Number is prime")
      break