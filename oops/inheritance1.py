class person(object):
    def __init__(self,name,id): # parameterised constructor
        self.name = name
        self.id = id
    def display(self):
        print(self.name,self.id)    

Emp = person("Prasad",47)
Emp.display()
 
class emp(person):
    def Print(self):
        print("Emp class called")
empDetails = emp("Mahesh babu",100)   
empDetails.display()
empDetails.Print()    


        