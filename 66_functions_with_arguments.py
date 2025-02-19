"""There are two types of functions in python :

1. Built in functions(Already present in python)
    E.G. len(),print(),range() etc.

2.User defined functions(Defined by the user) 
    E.G. def greet():
   user=input("Enter the user's name: ")
   print(f"Hello {user}")
greet()"""
#greets and keys = arguments
#values can be assigned like variable during function call.
def greet(greets,keys):
   user=input("Enter the user's name: ")
   print(f"Hello {user}. {greets}." )
   print(keys)
   return "Thank you"
a = greet("we hope you guys are well", "Here's your keys for room number 101")#(greets,keys)
print(a)
