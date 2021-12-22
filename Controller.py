# from Labs import Lab
from Filtering import Filterisation
from ForGraphics import ForGraphics
from NumberOfTaskInTest import NumberInTest
# from CompletedLabs import CompletedLab
# from CompletedTests import CompletedTest
#
# def thirdFunction():
#     newLab = Lab(Theme ='GR', DeadlineDate='2021-07-11', MaxLScore=12, Subject_ID=1)
#     Lab.addNewLabInBase(newLab)

def test():
    newFilter = Filterisation(id=1, subjectId=1, testId=1)
    road = newFilter.main()
    #print(numbers)

def forGraphic():
    # для графика
    newObject = ForGraphics(testId=1)
    scores,koeffs = newObject.main()
    print("Баллы:")
    print(scores)
    print("Коэффы:")
    print(koeffs)
    # получение очерёдности заданий
    newNumbers = NumberInTest(testId=1)
    numbers = newNumbers.setgetNumbersInTest()
    print(numbers)



