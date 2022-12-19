n=int(input("Enter a number : "))
fact=1
if(n<0):
    print("Please enter a positive number!")
elif(n==0):
    print("The factorial of 0 is : 1")    
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial  number " ,n ," is: ",fact)    