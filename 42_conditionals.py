#If elif else ladder
a= int(input("Enter age:"))

# 1st if statement
if(a%2==0):
   print("A is even")

#2nd if statement
if(100>=a>=10):
   print("You are eligible\nGood For you")
elif(5<=a<9 ):
   print("You are not eligible")
elif(a==9):
      print("1 year less to be eligible.")
else:
   print("You are dead")
#End of 2nd if statement

print("End of the program")