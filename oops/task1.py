# class employee(object):
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def employee_1(self):
#         print(self.name,self.age,self.salary)

#     def employee_2(self):
#         print(self.name,self.age,self.salary) 

# emp = employee("reddy",200,400000)          
# empDetails = employee("Prasad",111,10000)
# empDetails.employee_1()
# emp.employee_2()


 
# class student(object):
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def student1(self):
#         print(self.name,self.marks)
#     def student2(self):
#         print(self.name,self.marks)
# stu1 = student("Prasad",100)
# stu2 = student("reddy",99)
# stu1.student1()
# stu2.student2()


# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks 
#         print(self.name,self.marks)     
# stu1 = student("Prasad",100)
# stu2 = student("reddy",99)



class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        # print(self.name,self.age,self.salary)

    

emp = Employee("reddy",200,400000)          
empDetails = Employee("Prasad",111,10000)
print("Hello, %s And %s " %(emp.name,emp.salary))
