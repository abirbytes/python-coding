#Write a python function to remove a given word from a list and strip it at the same time.
l1=['Harry','Rohan','Subham','an']
def rem(l,word):
   n=[]
   for item in l1:
      if not(item==word):
         n.append(item.strip(word))
   return n
print(rem(l1,"an"))