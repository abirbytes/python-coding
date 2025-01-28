s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))#The reason the output is 2 instead of 3 is that in Python, 20 (integer) and 20.0 (float) are considered equal in terms of value, even though they are different types. When added to a set, they are treated as the same element.

#So, when you try to add 20 and 20.0 to the set, Python will recognize that they represent the same value, and only one of them will be stored. The string "20" is still considered a distinct element.

#Thus, the set will only contain two unique elements:

#20 (or 20.0, treated as the same)
"20" #(the string)