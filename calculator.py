from secrets import choice


def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("...SELECT OPERATION...")
print("1. ADDITON")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

while True:
    choice=input("Select the options out of 1. 2. 3. 4. ")
    if choice in ('1','2','3','4'):
        num1=float(input("Enter the first number = "))
        num2=float(input("Enter the second number = "))

        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))

        next_calculation=input("...ENTER YES FOR NEXT CALCULATION OTHERRWISE ENTER NO...")
        if next_calculation=="no":
            break
else:
    print("...INVALID INPUT...")
