
choice =1
while(choice):
    print("Enter 1: Addition")
    print("Enter 2: Substraction")
    print("Enter 3: Multiplication")
    print("Enter 4: Division")
    print("Enter 5: Exit")
    ch= int(input("Enter your choice"))
    if(ch==1):
        a=float(input("Enter first no.:"))   
        b =float(input("Enter secound no.:"))
        c=a+b
        print("Addition of two no.: ",c)
    elif(ch==2):
        a=float(input("Enter first no.:"))   
        b =float(input("Enter secound no.:"))
        c=a-b
        print("Substraction of two no.: ",c)
    elif(ch==3):
        a=float(input("Enter first no.:"))   
        b =float(input("Enter secound no.:"))
        c=a*b
        print("Multiplication of two no.: ",c)
    elif(ch==4):
        a=float(input("Enter first no.:"))   
        b =float(input("Enter secound no.:"))
        c=a/b
        print("Division of two no.: ",c)
    elif(ch==5):
        break
    choice=int(input("Press 1: Main menu..."))
