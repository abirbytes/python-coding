"""
sum(3)= 3+2+1
sum(n)=n + (n-1)+....+2+1
"""
# def sum(n):
#    return float(n + (n/2)*(n-1))

# n=int(input("Enter the number:"))
# print(sum(n))

def sum(n):
   if(n==1):
      return 1
   return sum(n-1) + n
print(sum(4))
