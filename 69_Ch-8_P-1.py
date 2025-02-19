# def greatest(a,b,c):
#    if(a>b and a>c):
#       return a
#    elif(b>a and b>c):
#       return b
#    else:
#       return c
# a=greatest(1,2,3)
# print(a)
n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))
n3=int(input("Enter the number:"))
def greatest():
   if(n1>n2 and n1>n3):
      print(f"The greatest number is {n1}")
   elif(n2>n1 and n2>n3):
      print(f"The greatest number is {n2}")
   else:
      print(f"The greatest number is {n3}")
greatest()
