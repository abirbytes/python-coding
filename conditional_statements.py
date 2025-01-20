                  ####Conditional Statements####
#statments in which we have a condition are known as conditional statements
'''Key words for conditional statements in python are if-elif-else
if(condition):
       Statement1
elif(condition):
      Statement2
else(condition): [used when elif and if not working]
      StatementN
Use 4 gaps for before statement as it comes in if known as indentation'''
#Rules of python are known as syntax

                #Example Code: Traffic Lights
'''light= input("The color of light is :")
if(light=="Red"):
   print("Stop")
elif(light=="Green"):
   print("Go")
else:
   print("Light is not working")'''

              #Example code : Grades for 10th graders....
'''Marks = input("Obtained marks in the exam: ")
if(Marks>="95"):
   print("A+")
elif(Marks >="90" and Marks < "95"):
   print("A")
elif(Marks>="85" and Marks < "90"):
   print("A-")
else:
   print("Better luck next time")'''

'''#variable = <val1> if <condition> else <val2> ////// single line if statement
food = input("food : ")
eat = "yes" if (food=="cake") else "no"
print(eat)
         #Another example : <str1> if <condition1 or 2> else <str2>
print("Wow") if food=="sweets" or food=='choco' else print("Not wow")'''
 
                #Clever if//Ternary operators (false,true)
                # Vote coding
'''age =int(input("My age is :"))
vote =("yes","no")[age<18]
print(vote)'''
               #Tax calculator
'''sal = float(input("My salary is :"))
tax = sal*(2,3) [sal<50]
print(tax)'''