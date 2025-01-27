# Properties of sets:
# 1. Sets are unordered > Element's order doesnt matter
# 2.Sets are unindexed > Cannot access elements by index
# 3.There is no way to change items in sets.
# 4.Sets cannot contain duplicate values
#5.Sets are mutable like lists
s={1,5,32,54,5,5,"Abir"}
s2={2,5,32,84,5,7,"Kabir"}
s.add(558)
print(s,type(s))
print(len(s))
s.remove(5)#Removes 5 from the set and updates it
print(s)
# s.clear()
# print(s)#Clears the set
s.add(56)
print(s)
# s2.pop()
# print(s2) Removes a random value from the set
print(s.union(s2))#Gives a set with all the elements of the