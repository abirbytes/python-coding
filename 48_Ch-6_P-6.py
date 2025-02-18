marks_of_the_student= int(input("Enter the marks of the student"))
if(90<=marks_of_the_student<=100):
   print("Excellent")
elif(80<=marks_of_the_student<90):
   print("A")
elif(70<=marks_of_the_student<80):
   print("B")
elif(60<=marks_of_the_student<70):
   print("C")
elif(50<=marks_of_the_student<60):
   print("D")
else:
   print("F")

print("Your grade is:" , marks_of_the_student)