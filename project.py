num1 = int(input("enter your first number :"))
num2 = int(input("enter your second number :"))
operation = input("enter your operation : ")

def cal(a,b,op):
    if( op == "+"):
        print("your sum is :" , a+b)
    elif( op == "-"):
        print('your difference is :', a -b)
    elif(op == "*"):
        print("your product is :" , a*b)
    elif(op == "/"):
        if(b != 0):
            print("your divison is :", a/b)
        else:
            print("error , can't divide by zero")
    elif(op == "%"):
        print("your remainder is :", a%b)
    else:
        print("not a valid operation")


cal(num1,num2,operation)