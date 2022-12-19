# n=int(input("enter a number. : "))
# total =0
# temp = n
# while(n!=0):
#     nw=n%10
#     total = nw*nw*nw + total
#     n=n//10
# print(total)    
# if(temp == total):
#     print("Armstrong number")
# else:
#     print("not an armstrong number")      


number=int(input("Enter the number:"))
sum=0
temp=number
while(temp>0):
    digit=temp %10
    # print(digit)
    sum+=digit**3
    # print(sum)
    temp //=10
    # print(temp)407

if(number==sum):
    print(number,"is an armstrong number")
else:
    print(number,"is not a armstrong number")