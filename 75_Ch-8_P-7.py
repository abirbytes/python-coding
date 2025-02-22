def mult(n,i=1):
   if (i>10):
      return
   print(n*i)
   mult(n,i+1)
   
print(mult(5))