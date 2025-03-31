# Task 1 - Perform Basic Mathematical operations

'''a=float(input("Enter the first number : "))
b=float(input("Enter the second number :"))
if (a or b) <0:
    print("This is a invalid input")
else:
    q=input("Which operation to perform +.-.* or / : ")
  if q == '+':
        print(f'The addition of the two numbers {a} and {b} is : {a+b}')
elif q == '-':
        print(f'The subtraction of the two numbers {a} and {b} is : {a - b}')
elif q == '*':
        print(f'The multiplication of the two numbers {a} and {b} is : {a * b}')
elif q == '/':
    if b<=0:
        print("The denominator cannot be 0")
    else:
            print(f'The division of the two numbers {a} and {b} is : {a / b}')
else:
        print("the input is invalid")'''

 #CREATE A PERSONALISED MESSAGE BY TAKING INPUT OF NAME
print( "The program will ask for your name first")
firstname=input("Please enter your first name : ")
secondname=input("Please enter your second name : ")
name = firstname +  secondname
print(f'Hello {name}!, welcome to the Python program')