num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
Operation=input("Enter the operator that need to be performed:")
if Operation == "+":
    print(f"The addition of 2 numbers:{num1+num2}")
elif Operation == "-":
    print(f"The subtraction of 2 numbers:{num1-num2}")
elif Operation == "*":
    print(f"The multiplication of 2 numbers:{num1*num2}")
elif Operation == "/":
    print(f"The division of 2 numbers:{num1/num2}")
else:
    print("Enter the valid Operators")