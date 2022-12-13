# car=int(input("Number of Cars"))
# bike=int(input("Number of bikes"))
# carpayment=car*40 
# bikepayment=bike*20
# total=carpayment+bikepayment
# print("car : ",carpayment)
# print("bike : ",bikepayment)
# print("Total amount : ",total)

# car="devi"
# print()


n=int(input("Product quantity 1 :"))
m=int(input("Product quantity 2 :"))
l=int(input("Product quantity 3 :"))
product1=40
product2=50
product3=60
if(n>1):
    total=n*product1+n*product2+n*product3
    print("the payment for product 1is", n*product1)  
    print("the payment  for product 2 is", m*product2)  
    print("the payment  for product 3 is", l *product3)  
    print("the total quantities are:",m+n+l)
    print("the total payment is \n", total)
else:
    print("please enter correct value")     
     
