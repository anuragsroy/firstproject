class Employee:
    def __init__(self,empid,ename,salary):
        self.empid=empid
        self.ename=ename
        self.salary=salary

    def printEmployee(self):
        print("empid:",self.empid)
        print("ename:",self.ename)
        print("salary:",self.salary)


e=Employee(1,'abc',99000)
e.printEmployee()