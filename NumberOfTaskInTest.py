from Tests import Test

class NumberInTest:

    dictOfNumbers = {}
    def __init__(self, testId):
        self.testId = testId

    def setNumbersInTest(self):
        test = Test.getListOfAllTasksInTestIds(self.testId)
        count = 1
        for i in test:
            self.dictOfNumbers[i] = count
            count += 1

    def getNumbersInTest(self):
        return self.dictOfNumbers

    def setgetNumbersInTest(self):
        self.setNumbersInTest()
        return self.getNumbersInTest()
