choice=1
while(choice!=0):
    n=int(input("Enter the number:"))
    if n<0:
        print(n,"is negative")
    elif n>0:
        print(n,"is positive")
    else:
        print("zero is a neutral number")
    choice=int(input("do you want to continue 1/0:"))
