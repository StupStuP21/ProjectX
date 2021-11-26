import Labs
import Students


def thirdFunction():
    newLab = Labs.Lab(Theme ='GR', DeadlineDate='2021-07-11', MaxLScore=12, Subject_ID=1)
    Labs.Lab.addNewLabInBase(newLab)

def test():
    newStud = Students.Student("Петров Василий Иваныч","ПИ",2)
    Students.Student.addNewStudentInBase(newStud)