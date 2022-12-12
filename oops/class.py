class Car: #Creating Car Class
    attr1 = "Adui"
    attr2 = "BMW"
    attr3 = "Range Rover"

    def names(self): #Creating Function
        print("The car name is : ", self.attr1)
        print("The car name is : ", self.attr2)
        print("The car name is : ", self.attr3)
myCar = Car() #Creating myCrae is object and Car is class
print(myCar.attr1) #Calling and printing only one variable
myCar.names() #Calling the function