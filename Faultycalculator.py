print("welcome to first faulty calculator: \nThis is developed by RAJ")


print("NOTE - If you type 56+9 , 45*3 ,and 56/6 then value will show 77,555,4.")

operation = input('''
please type math operation you would liketo complete:
+ for addition
- for subtraction
/ for division
* for multiplication
** for power
% for modulo

enter  your choice
''')
Number1=int(input("Please,Enter Your First Number,"))
Number2=int(input("Please Enter Your Second Number,"))


if operation == "+" and Number1 == 56 and Number2 == 9 :
    print(77)
elif operation == "+":
    print (Number1+Number2)
elif operation == "-":
     print (Number1-Number2)
if operation == "*" and Number1 == 45  and Number2 == 3 :
    print (555)
elif operation == "*":
    print (Number1*Number2)
if operation == "/" and Number1 == 56 and Number2 == 6:
    print(4)
elif operation == "/":
    print (Number1/Number2)
elif operation == "**":
    print(Number1**Number2)
elif operation == "%":
    print(Number1%Number2)





else:
    print("Thank U For Using Faulty Calculator")



