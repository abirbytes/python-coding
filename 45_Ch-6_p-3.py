# s1= "Make a lot of money"
# s2="Buy now"
# s3="Subscribe this"
# s4="Click this"
# message = input("Enter the message:")
# if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
#    print("Spam")
# else:
#    print("Non-spam")
spams = input("Spam comments or keywords:")
if(spams=="Make a lot of money" or spams=="Buy Now" or spams=="Subscribe this" or spams=="Click this"):
   print("Spam")
else:
   print("Non-Spam")
