# from Labs import Lab
from Filtering import Filterisation
from ForGraphics import ForGraphics
from taskWsDto import getTaskWsDtoListMock2
from NumberOfTaskInTest import NumberInTest


def test():
    #zadaniya
    newFilter = Filterisation(id=1002, subjectId=2, testId=2)
    road = newFilter.main()
    #print(numbers)

def forGraphic():
    # для графика

    newObject = ForGraphics(testId=2)
    scores,koeffs = newObject.main()

    #scores, koeffs = [1,2,3,4,5],[5,4,3,2,1]
    return scores, koeffs



def forTest(road,testId):
    numberOfTasksInTest = NumberInTest(testId).setgetNumbersInTest()
    return getTaskWsDtoListMock2(road, numberOfTasksInTest)





