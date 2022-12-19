entries=int(input("Enter the entries:"))
n1,n2=0,1
count=0
if(entries<=0):
    print("Please enter the positive number")
elif(entries==1):
    print("fabnoseries upto",entries)
    print(n1)
else:
    print("fibnoseries ")
    while(count<entries):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1