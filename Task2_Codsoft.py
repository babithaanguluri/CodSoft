print("SIMPLE CALCULATOR")
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y ==0:
        return "Error! Division by Zero."
    return x/y

print("\nSelect the options given below")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("0.Exit")
while True:
    choice = input("Enter the operator(0,1,2,3,4):")
    if choice =='0':
        print("Exiting the calculator...")
        break
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice =='1':
            print(num1, "+", num2,"=",add(num1,num2))
        elif choice =='2':
            print(num1,"-", num2,"=",subtract(num1,num2))
        elif choice =='3':
            print(num1, "*", num2, "=",multiply(num1,num2))
        elif choice == '4':
            print(num1,"/", num2, "=",divide(num1,num2))
    else:
        print("Invalid input! Select a valid option.") 