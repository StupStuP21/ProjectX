from Filtering import Filterisation
from Tests import Test
from CompletedTasks import CompletedTask
from CompletedTests import CompletedTest


class ForGraphics:
    roads_for_all = []
    koefs_for_all = []
    scores_for_all = []

    def __init__(self, testId):
        self.TestId = testId
        self.TestObject = Test.getTestById(self.TestId)
        self.AllStudents = CompletedTest.getAllStudentsWithCompletedTest(self.TestId)
        print(len(self.AllStudents))
        # self.roads_for_all = self.setRoadsForAllStudentsWithTest()

    def setRoadsForAllStudentsWithTest(self):
        roads = []
        for i in self.AllStudents:
            newFilter = Filterisation(i.Student_Id, self.TestObject.Subject_ID, self.TestObject.Test_ID)
            self.roads_for_all.append(newFilter.main())
            # roads.append(newFilter.main())
        # return roads

    # -----------------------------------------------
    # -------Коэффициент выполнения дороги-----------
    # -----------------------------------------------
    # Берём полученное кол-во баллов за каждое задание (1)
    # Берём приоритет задания (место в дороге) (2)
    # Берём макс балл за задание (3)
    # Коэф для каждого задания у одного студента = ((1)*(2))/(2*3)) (5)
    # Общий коэфф для студента = сумма всех (5) / кол-во заданий в тесте
    # -----------------------------------------------
    def setKoefs(self):
        numberOfTasks = len(self.roads_for_all[0])
        studCounter = 0

        for i in self.AllStudents:
            # percentsOfCompleting = []
            koeffsForCurrent = []
            endingKoefForCurrent = 1
            taskCounter = 0
            for j in self.roads_for_all[studCounter]:
                complTask = CompletedTask.getCompletedTaskByIdInTest(i, j, self.TestId)
                # percentsOfCompleting.append(complTask.GetTaskScore / j.MaxTScore)
                prioritet = numberOfTasks - taskCounter
                koeffsForCurrent.append(
                    (complTask.GetTaskScore * prioritet) / (prioritet * j.MaxTScore))
                # (percentsOfCompleting[taskCounter] * prioritet) / (prioritet*j.MaxTScore))
                taskCounter += 1

            for x in koeffsForCurrent:
                endingKoefForCurrent += x
            endingKoefForCurrent /= len(self.roads_for_all[0])

            self.koefs_for_all.append(endingKoefForCurrent)
            studCounter += 1

    def setScoresForTests(self):
        for i in self.AllStudents:
            self.scores_for_all.append(CompletedTest.getCompletedTestByStudIdAndTestId(i, self.TestObject).GetTScore)

    def main(self):
        self.setRoadsForAllStudentsWithTest()
        self.setKoefs()
        self.setScoresForTests()
        return self.scores_for_all, self.koefs_for_all
