#Basically assigns the value of key argument by default and lets it use the same value by default. But if we assign  any value during the function call for the argument it will not use the default one.

def greet(welcome,keys="Room No.101"):
   user=input("Enter the user's name: ").capitalize()
   print(f"Hello {user}. {welcome}." )
   print(keys)
greet("Hope you're well")
greet("Hope you are well", "102") #Not uses the default value for the argument keys