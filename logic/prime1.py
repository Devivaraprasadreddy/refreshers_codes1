user = int(input("enter a number : "))
if(user>1):
    for i in range(2,user):
        if(user%i==0):
            print(user," is not a prime number")
            print(i, "times ",user//i,"is",user)
            break
    else:
        print(user, " is a prime number") 
else:
    print(user,"is not a prime number")                       