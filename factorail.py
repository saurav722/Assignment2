num=int(input("Enter the number = "))
factorial=1
if num<0:
    print("Factorial of any negative number doesn't exist.")
elif num==0:
    print("Factorial of 0 is 0.")
elif num==1:
    print("Factorial of 1 is 1.")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)    
     
