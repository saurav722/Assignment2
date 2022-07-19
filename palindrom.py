# s=input(("Enter a letter:"))  
# s1=s[::-1]
# if s1==s: 
#       print("The letter is a palindrome")  
# else:  
#       print("The letter is not a palindrome")  


num=int(input("Enter a number:"))  
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if (temp==rev):
    print("value is palindrom")
else:
    print("value is not palindrom")
    