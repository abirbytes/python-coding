#No.1>>.What is function? - The part containing the exact set of instructions which are executed during the function call>
#NO.2>>>.A function is a group of statements performing a specific task.
#No.3>>>.When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
#No.4>>>.A function can be reused by programmer in a given program any number of times
#Function definition 
def avg():#The part containing the exact set of instructions which are executed during the function call>
   a=int(input("Enter the number:"))
   b=int(input("Enter the number:"))
   c=int(input("Enter the number:"))
   average = (a+b+c)/c
   print(average)
#Whenever we want to call a function, we put the name of the function followed by parenthesis as follows:
avg()#Function Call
print("Thank You")#Prints thank you after the first function call but not after the other
avg()

