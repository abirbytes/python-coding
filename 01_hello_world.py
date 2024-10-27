#Asks user what is your name?
name = input("What is your name?") 
#Remove blank whitespace from str & Capitalize users name (chain up)
name = name.strip().capitalize()
# f gives a hint to python to treat the function specially.
print(f"Hello, {name}")

