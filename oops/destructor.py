class Employee: #Creating Class
    def _init_(self): # Initializing
        print("Employee Created")
    def _del_(self): # Deleting (Calling destructor)
        print("Employee Deleted")

#Craeting an object
emp = Employee()
del emp
emp = Employee()