"""noOfCars=0
noOfCars=0
total_sum=0
cars=int(input())
bikes=int(input())
amount_cars=cars*40
amount_bikes=bikes*20
total_sum=amount_cars+amount_bikes
print("The total cars parked", cars)
print("The total bikes parked",bikes)
print("The amount for cars parked", amount_cars)
print("The amount for bikes parked", amount_bikes)
print("The total amount for both cars and bikes is : ",total_sum)"""
# another ques 
product1 = int(input("Enter how many apples did the buyer want : "))
product2 = int(input("Enter how many kiwi did the buyer want : "))
product3 = int(input("Enter how many grapes did the buyer want : "))
product4 = int(input("Enter how many oranges did the buyer want : "))
product5 = int(input("Enter how many bananna did the buyer want : "))

amountforp1=product1*100
amountforp2=product2*200
amountforp3=product3*300
amountforp4=product4*400
amountforp5=product5*500

#for loop
# l=[product1,product2,product3,product4,product5]
# for i in l:
#     print(i, sep=' ', end='\n')

if((product1<=0) or (product2<=0) or (product3<=0) or (product4<=0) or (product5<=0)) :
    print("Please enter a positive number")
else: 
    totalAmount = amountforp1+amountforp2+amountforp3+amountforp4+amountforp5
    entries = {product1:100, product2:200, product3:300, product4:400, product5:500}
    x = open("mydata.txt","a")
    # file=x
    print("the amount of all products",entries,file=x)
    
    # x.close()

    entries1 = {product1:amountforp1, product2:amountforp2, product3:amountforp3, product4:amountforp4, product5:amountforp5}
    for k,v in entries.items():
        print(k, v)
    print(entries1)
    print("The total amout should be paid by the user is: ", totalAmount)