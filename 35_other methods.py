s1={1,5,32,54,5,5,"Abir"}
s2={2,5,32,84,5,7,"Kabir"}
#print(s1.union(s2))
# >>>
# #Gives a set with all the elements of the sets without repeating 

print(s1.intersection(s2))#Makes a set with only commpn values in both sets

set3 = {1, 2, 3}
set4 = {3, 4, 5}
result = set3.difference(set4)  # or set3 - set4
print(result)  # Output: {1, 2}Returns a set with elements that are in the first set but not the second.
set5 = {1, 2}
set6 = {1, 2, 3}
result = set6.issuperset(set5)
print(result)  # Output: True
result2 = set5.issubset(set6)
print(result2)
