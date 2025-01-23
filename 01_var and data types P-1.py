# comma in lines helps to combine two sentences
print("My name is Abir", "My age is 17")
name = "Abir" # Quotes are used for string remaining constant
a = None
age = 17#int
old = False
weight = 144.05#float (decimals)
print(age) #Never use "" to get the value of variable
print("My name is :", name)
print("My age is :", age) #here string is the same, the age is acc to the value
age2 = age + 1 # similar to a = b
print(age)
#type can detect the type of value in the variable in python..
print(type(name))
print(type(age))
print(type(weight))
#Data Types :
#Int : all negative and positive whole numbers
#Strings : all letters or combination of letters in the ""
#Float : Contains Decimals
#Boolean : True or False [First letter should be in capital letter]
#None : a=none
print(type(a))
print(type(old))
#Summation
b = 3
c = 8
sum = (b+c)
diff = (b-c)
print(diff)
# Punctuators are the symbols to keep codes organized
# Python is a typed inplicit language, not to mention data type;int.name = 23 xxxx
#Expression Execution
A,B = -6,3
F = B%A
C,D = 5,6.00
E = D/C # Two division sign means integer division; turns the value to closest floating value.....
txt = "@"
print(2*txt*3)#String and numeric values can be operated together by multiplication..
#print((A+txt) * B) # One string can be added only with another string...
#Numeric Values Can Operate with all arithmetic operations; +,-,*,/ etc...
print(A+B*C-D)
#Arithmetic expressions with int or float will be = float
print(C*D)
print(C+D)
#Integer divided by integer will result in floating value....
print(A/B)
print(E , D/C) # Two division sign means integer division; turns the value to closest floating value..... one division results exact floating value...
#floor gives the closest integer which is less or equal to the float value...
# (A//B) = floor(A//B)
A,B = -6,3
F = B%A
print(F)# Remainder or % modulo is negative only when denominatore is negative...
Name = input("Name:") # Quotes are used for string remaining constant
Age = int(input("Age:")) #int
Weight = float(input("Weight:"))
print("My name is", Name, "and my age is", Age, "Also, my weight is" , Weight ,"Kgs")
#Identifiers are always a-z or A - Z and cant start with digits, and identifiers are functions and variables
# ** is a valid arithmetic operator in python as a**b = a^b
#Logical operators in python = and, or, not
#"in" is a membership operator in python
