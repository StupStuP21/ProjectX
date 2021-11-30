from Labs import Lab
from CompletedLabs import CompletedLab
from CompletedTests import CompletedTest

def thirdFunction():
    newLab = Lab(Theme ='GR', DeadlineDate='2021-07-11', MaxLScore=12, Subject_ID=1)
    Lab.addNewLabInBase(newLab)

def test():
    newCompletedTest = CompletedTest(1,1,5)
    newCompletedTest.addNewInBase(newCompletedTest)