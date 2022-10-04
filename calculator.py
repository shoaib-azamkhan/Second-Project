num1=int(input("enter your first number :"))
num2=int(input("enter your second number :"))
operator=input("what you want to do like (+ , - , * , /) :")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)  
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("you are going wrong bro.")