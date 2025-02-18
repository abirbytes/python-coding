total_marks= int(input("Total marks in 3 subjects can be gained:"))
s1= int(input("Marksin s1:"))
s2= int(input("Marks in s2:"))
s3= int(input("Marks in s3:"))
s_m = (s1+s2+s3)
percent = (s_m/total_marks)*100
if(percent>=40 and s1>=33 and s2>=33 and s3>=33):
   print("Passed")
else:
   print("Failed")
