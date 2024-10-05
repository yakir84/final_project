from class_person import Person
import utils

class Student(Person):
    def __init__(self):
        super().__init__()


    def getFieldOfStudy(self):
        return self.field_of_study
    

    def setFieldOfStudy(self, field_of_study):
         self.field_of_study = field_of_study
    

    def getYearOfStudy(self):
        return self.year_of_study
    

    def setYearOfStudy(self, year_of_study):
        self.year_of_study = year_of_study
    

    def getScoreAvg(self):
        return self.score_avg
    

    def setScoreAvg(self, score_avg):
        self.score_avg = score_avg


    def userSurvey(self):
        if not super().userSurvey():
            return False
        self.field_of_study = input("what are you studying? ")
        self.year_of_study = input("What is your study year? ")
        if not utils.isDigit(self.year_of_study):
            return False
        self.year_of_study = int(self.year_of_study)
        self.score_avg = input("What is your average score? ")
        if not utils.isDigit(self.score_avg):
            return False
        self.score_avg = float(self.score_avg)
        return True
    

    def printPersons(self):
        super().printPersons()
        print("  Field of study: " + self.getFieldOfStudy())
        print("  Year of study: " + str(self.getYearOfStudy()))
        print("  Score avg: " + str(self.getScoreAvg()))
    

    def getPersonDict(self):
        row = super().getPersonDict()
        row["Field of study"] = self.getFieldOfStudy()
        row[ "Year of study"] = self.getYearOfStudy()
        row["Score avg"]  = self.getScoreAvg()
        return row
        


    def printStudent(self):
        print(self.getPersonString() + ", The field of study is " + self.getFieldOfStudy() + ", the yaer of study is " + str(self.getYearOfStudy()) + ", the avg of student is " + str(self.getScoreAvg()))


if __name__ == "__main__":
    test_field_of_study = "Software developer"
    test_year_of_study = 2
    test_score_avg = 40
    student = Student(test_field_of_study, test_year_of_study, test_score_avg)
    if Student.getFieldOfStudy() != test_field_of_study:
        print("Error: ID should be " + str(test_field_of_study) + " but i got " + str(Student.getId()))
    if Student.getYearOfStudy() != test_year_of_study:
        print("Error: Name should be " + test_year_of_study + " but i got " + str(Student.getName()))
    if Student.getScoreAvg() != test_score_avg:
        print("Error: Age should be " + str(test_score_avg) + " but i got " + str(Student.getAge()))