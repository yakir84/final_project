import utils
import pandas as pd

class Person:

    
    def __init__(self):
        pass


    def getId(self):
        return self.id
    

    def setId(self, user_id):
        self.id = user_id


    def getName(self):
        return self.name


    def setName(self, user_name):
        self.name = user_name


    @staticmethod
    def isEven(num):
        return num % 2 == 0

    
    def getAge(self):
       return self.age
    
  
    def setAge(self, user_age):
        self.age = user_age

    def getPersonString(self):
         return "His ID is " + str(self.getId()) + " and his name is " + self.getName() + " and is " + str(self.getAge()) + " years old"


    def userSurvey(self):
        self.id = input("ID: ")
        if not utils.isDigit(self.id):
            return False
        self.id = int(self.id)
        self.name = input("Name: ")
        self.age = input("Age: ")
        if not utils.isDigit(self.age):
            return False
        self.age = int(self.age)
        return True
        

    def printPersons(self):
        print("  ID: " + str(self.getId()))
        print("  Name: " + self.getName())
        print("  Age: " + str(self.getAge()))

    
    def getPersonDict(self):
        row = {
        "ID": self.getId(),
        "Name": self.getName(),
        "Age": self.getAge()
    }
        return row


if __name__ == "__main__":
    test_id = 100
    test_name = "test name"    
    test_age = 40
    person = Person(test_id, test_name, test_age)
    if person.getId() != test_id:
        print("Error: ID should be " + str(test_id) + " but i got " + str(person.getId()))
    if person.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + person.getName())
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))






    




    