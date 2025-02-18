for i in range(100):
   if(i==68):
      break #Exit the loop right now
   print(i)

for j in range(20):
   if(j==16):
      continue#only skip the value and print from 17 again
   print(j)

#Pass statement
for k in range(25):
   pass #ignores it; is a null statement skips it
k=0
while(k<20):
   print(k)
   k+=1