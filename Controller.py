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
    #zadaniya
    newFilter = Filterisation(id=1, subjectId=1, testId=1)
    road = newFilter.main()
    #print(numbers)

def forGraphic():
    # для графика
    """
    newObject = ForGraphics(testId=1)
    scores,koeffs = newObject.main()
    """
    scores, koeffs = [1,2,3,4,5],[5,4,3,2,1]
    return scores, koeffs




