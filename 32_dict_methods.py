marks={
   "Abir": 100,
   "Lamia" : 90,
   "Tam":80,
   0:"Abir"
}
#print(marks.item())
#>>>
# Gives us the dictionary in form of tuples and let us know how many items are there

# print(marks.keys()) 
#>>>
# Gives us all the keys of the dictionary mentioned in it

#print(marks.values())
#Gives us all the values of the keys mentioned in the dictionary

# marks.update({"Lamia":99,"Tam":88,"Nasif":"Namira"})
# print(marks)

print(marks.get("Abir"))#if wrong gives none
print(marks["Abir"])#If wrong gives error