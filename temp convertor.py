a=float(input("Enter the temputer to convert into degree= "))
b=float(input("Enter the temputer to convert into fahrenheit= "))
while(1):

    print("Enter 1 for convert degree to fahrenheit")
    print("Enter 2 for convert fahrenheit to degree")
    print("Enter 3 for Exit")
    c=int(input("Enter your chioce"))
    if(c==1):
        float d=(a*(9/5)+32)
        print(a,"is convert into fahrenheit=" ,d)
    elif(c==2):
        float d=(b-32)*(5/9)
        print(b,"is convert into degree=" ,d)
    else:
        print("Exit")




