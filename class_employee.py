from class_person import Person
import utils

class Employee(Person):
    def __init__(self):
        super().__init__()
       

    def getFieldOfWork(self):
        return self.field_of_work
    

    def setFieldOfWork(self, field_of_work):
        self.field_of_work = field_of_work


    def getSalary(self):
        return self.salary
    

    def setSalary(self, salary):
        self.salary = salary


    def userSurvey(self):
        if not super().userSurvey():
            return False
        self.field_of_work = input("What is your line of work? ")
        self.salary = input("What is your monthly salary? ")
        if not utils.isDigit(self.salary):
            return False
        self.salary = int(self.salary)
        return True
    

    def printPersons(self):
        super().printPersons()
        print("  Working: " + self.getFieldOfWork())
        print("  Salary: " + str(self.getSalary()))


    def getPersonDict(self):
        row = super().getPersonDict()
        row["Field of work"] = self.getFieldOfWork()
        row["Salary"] = self.getSalary()
        return row


    def printEmployee(self):
        print(self.getPersonString() + ", His field of activity is " + self.getFieldOfWork() + " and his salary is " + str(self.getSalary())) 


if __name__ == "__main__":
    test_field_of_work = "Software developer"
    test_salary = 50000    
    employee = Employee(test_field_of_work, test_salary)
    if Employee.getFieldOfWork() != test_field_of_work:
        print("Error: ID should be " + str(test_field_of_work) + " but i got " + Employee.getFieldOfWork())
    if Employee.getSalary() != test_salary:
        print("Error: Name should be " + test_salary + " but i got " + str(Employee.getSalary()))