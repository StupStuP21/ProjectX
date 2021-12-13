# from Labs import Lab
from Filtering import Filterisation


# from CompletedLabs import CompletedLab
# from CompletedTests import CompletedTest
#
# def thirdFunction():
#     newLab = Lab(Theme ='GR', DeadlineDate='2021-07-11', MaxLScore=12, Subject_ID=1)
#     Lab.addNewLabInBase(newLab)

def test():
    newFilter = Filterisation(id=1, subjectId=1, testId=1)
    road = newFilter.main()


