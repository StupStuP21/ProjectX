import datetime
import math

#import CompletedLabs
import Labs
import Tasks
from Labs import Lab
from Students import Student
from Tests import Test
from CompletedTasks import CompletedTask
from CompletedLabs import CompletedLab


nNearest = 3


class Filterisation:
    AllCompletedLabsWithoutCurrent = ...
    AllCompletedLabsCurrent = ...

    def __init__(self, id, subjectId, testId):
        self.currentStudentId = id
        self.subjectId = subjectId
        self.AllStudentsWithoutCurrent = Student.getStudentsWithoutById(self.currentStudentId)
        self.currentStudent = Student.getStudentById(self.currentStudentId)
        self.AllCompletedLabs = Lab.getAll_in_Subject(self.subjectId)
        self.AllCompletedLabs = CompletedLab.getAllCompletedLabs()
        self.Test_Id = testId
        self.Test = Test.getTestById(testId)
        self.AllTasks = ...
        self.AllCompletedTasks = ...  # возможно, не сюда, а потом для каждого отдельно

    @staticmethod
    def normilizingCompletedLabsData(labs):  # labs - list of labs
        wCurrentTryesMax = 0
        wCurrentTryesMin = 0
        wCurrentDateMax = labs[0].PassDate
        wCurrentDateMin = labs[0].PassDate
        wCurrentScoreMax = 0
        wCurrentScoreMin = 0
        for i in labs:
            i.PassDate = datetime.date(wCurrentDateMax.year,i.PassDate.month,i.PassDate.day)
            if i.GetLScore > wCurrentScoreMax:
                wCurrentScoreMax = i.GetLScore
            elif i.GetLScore < wCurrentScoreMin:
                wCurrentScoreMin = i.GetLScore

            if i.PassDate > wCurrentDateMax:
                wCurrentDateMax = i.PassDate
            elif i.PassDate < wCurrentDateMin:
                wCurrentDateMin = i.PassDate

            if i.Tryes > wCurrentTryesMax:
                wCurrentTryesMax = i.Tryes
            elif i.Tryes < wCurrentTryesMin:
                wCurrentTryesMin = i.Tryes
        difMinMax_For_Tryes = wCurrentTryesMax - wCurrentTryesMin
        diffMinMax_For_Date = wCurrentDateMax - wCurrentDateMin
        diffMinMax_For_Score = wCurrentScoreMax - wCurrentScoreMin
        if (diffMinMax_For_Score!=0 and diffMinMax_For_Date!=0 and difMinMax_For_Tryes!=0):
            for i in labs:
                i.Tryes = (i.Tryes - wCurrentTryesMin) / difMinMax_For_Tryes
                i.PassDate = (i.PassDate - wCurrentDateMin) / diffMinMax_For_Date
                i.GetLScore = (i.GetLScore - wCurrentScoreMin) / diffMinMax_For_Score
        elif (diffMinMax_For_Score!=0 and diffMinMax_For_Date!=0 and difMinMax_For_Tryes==0):
            for i in labs:
                i.Tryes = 1
                i.PassDate = (i.PassDate - wCurrentDateMin) / diffMinMax_For_Date
                i.GetLScore = (i.GetLScore - wCurrentScoreMin) / diffMinMax_For_Score
        elif (diffMinMax_For_Score!=0 and diffMinMax_For_Date==0 and difMinMax_For_Tryes!=0):
            for i in labs:
                i.Tryes = (i.Tryes - wCurrentTryesMin) / difMinMax_For_Tryes
                i.PassDate = 1
                i.GetLScore = (i.GetLScore - wCurrentScoreMin) / diffMinMax_For_Score
        elif (diffMinMax_For_Score==0 and diffMinMax_For_Date!=0 and difMinMax_For_Tryes!=0):
            for i in labs:
                i.Tryes = (i.Tryes - wCurrentTryesMin) / difMinMax_For_Tryes
                i.PassDate = (i.PassDate - wCurrentDateMin) / diffMinMax_For_Date
                i.GetLScore = 1
        elif (diffMinMax_For_Score!=0 and diffMinMax_For_Date==0 and difMinMax_For_Tryes==0):
            for i in labs:
                i.Tryes = 1
                i.PassDate = 1
                i.GetLScore = (i.GetLScore - wCurrentScoreMin) / diffMinMax_For_Score
        elif (diffMinMax_For_Score==0 and diffMinMax_For_Date!=0 and difMinMax_For_Tryes==0):
            for i in labs:
                i.Tryes = 1
                i.PassDate = (i.PassDate - wCurrentDateMin) / diffMinMax_For_Date
                i.GetLScore = 1
        elif (diffMinMax_For_Score==0 and diffMinMax_For_Date==0 and difMinMax_For_Tryes!=0):
            for i in labs:
                i.Tryes = (i.Tryes - wCurrentTryesMin) / difMinMax_For_Tryes
                i.PassDate = 1
                i.GetLScore = 1
        else :
            for i in labs:
                i.Tryes = 1
                i.PassDate = 1
                i.GetLScore = 1

    @staticmethod
    def cosMetric(complLabOne, complLabTwo):
        sqrtSumOne = math.sqrt(
            math.pow(complLabOne.GetLScore, 2) + math.pow(complLabOne.PassDate, 2) + math.pow(complLabOne.Tryes, 2))
        sqrtSumTwo = math.sqrt(
            math.pow(complLabTwo.GetLScore, 2) + math.pow(complLabTwo.PassDate, 2) + math.pow(complLabTwo.Tryes, 2))
        vectorMultOne = complLabOne.GetLScore * complLabOne.PassDate * complLabOne.Tryes
        vectorMultTwo = complLabTwo.GetLScore * complLabTwo.PassDate * complLabTwo.Tryes
        return (vectorMultOne * vectorMultTwo) / (sqrtSumOne * sqrtSumTwo)

    def getAllComplLabsForCurrentStud(self, sId):
        labsList = []
        for i in self.AllCompletedLabs:
            if i.Stud_ID == sId and Labs.Lab.getLabById(i.Lab_ID).Subject_ID == self.subjectId:
                labsList.append(i)
        return labsList

    # лабы надо сортировать по lab_id в обоих списках сданных лаб
    # надо пересмортреть циклы, от чего отталкиваться
    # предполагается, что, если чел даж не сдал лабу, в сданных лабах инфа об этом всё равно будет (прост всё по-минимуму стоять будет)
    def getNeighbors(self):
        Filterisation.normilizingCompletedLabsData(self.AllCompletedLabs)
        # self.normilizingCompletedLabsDataForCurrent()  # нормализуем факторные даннные в сданных лабах проверяемого студента
        self.AllCompletedLabsCurrent = self.getAllComplLabsForCurrentStud(self.currentStudentId)
        dists = {}  # словарь расстояний меж студентами (id другого студента,dist)
        for i in self.AllStudentsWithoutCurrent:
            #notCurLabs = CompletedLab.getAllCompletedLabsByStudId(i.Student_Id)  # все сданные лабы другого студента
            notCurLabs = self.getAllComplLabsForCurrentStud(i.Student_Id)
            if (len(notCurLabs) == 0):
                continue
            notCurLabsThatHaveCur = []  # все сданные лабы другого студента, которые есть у проверяемого
            for k in self.AllCompletedLabsCurrent:
                for j in notCurLabs:
                    if k.Lab_ID == j.Lab_ID:
                        notCurLabsThatHaveCur.append(j)
                        break
            # Filterisation.normilizingCompletedLabsData( notCurLabsThatHaveCur)  # нормализауем факторные данные в сданных лабах у другого студента
            dist = 0
            for k in range(len(notCurLabsThatHaveCur)):
                dist += Filterisation.cosMetric(self.AllCompletedLabsCurrent[k], notCurLabsThatHaveCur[k])
            dists[i.Student_Id] = dist
        sorted_tuples = sorted(dists.items(), key=lambda item: item[1])
        sorted_dists = {k: v for k, v in sorted_tuples}  # сортируем словарь дистанций по возрастанию
        NearestStudents = []
        s_id = sorted_dists.keys()
        count = 0
        for i in s_id:
            if count == nNearest:
                break
            for j in self.AllStudentsWithoutCurrent:
                if j.Student_Id == i:
                    NearestStudents.append(j)
            count += 1
        return NearestStudents

    def GetCompletedTasks(self, NearestStuds):  # получить лист листов выполненных заданий для каждого студента
        AllTasksForEachNearestStuds = []
        for i in NearestStuds:
            AllTasksForEachNearestStuds.append(CompletedTask.getAllCompletedTasksInTest(i, self.Test_Id))
        return AllTasksForEachNearestStuds

    def GetTasks(self, listOfCompletedTasks):
        listOfIds = []
        for i in listOfCompletedTasks[0]:
            listOfIds.append(i.Task_Id)
        AllTasks = Tasks.Task.getAllTasksInTestByTaskId(listOfIds)
        return AllTasks

    def GetListOfTasks(self, listOfTaskIds):
        listOfTaskIds = listOfTaskIds
        listOfTasks = []
        for i in listOfTaskIds:
            listOfTasks.append(Tasks.Task.getTasksById(i))
        return listOfTasks

    # ------------------------------------------------
    # идеально было бы вывести коэфф для сортировки по нему
    # ------------------------------------------------
    # для каждого задания посчитать сумму полученных баллов (1)
    # для каждого задания взять сложность (2)
    # для каждого задания взять максы, что можно за него получить (3)
    # коэф = ((1)+(2))/(3)
    # ------------------------------------------------
    # или
    # ------------------------------------------------
    # взять средний балл каждого выполненного задания (1)
    # взять максы по каждому заданию (2)
    # коэфф = (1)/(2) -- (3)
    # взять сумму полученных баллов для каждого задания (4)
    # взять сложности для каждого задания (5)
    # и потом сортировать по значению = ((3)*(4))/(5)
    # ------------------------------------------------
    # возвращает список id заданий
    # ------------------------------------------------
    def GetRoad(self, listOfObjectsOfCompletedTasks, listOfObjectsOfTasks):
        Road = {}
        maxScoresOfTasks = []  # список макс баллов, которое можно получить за каждое задание
        difficultiesOfTasks = []  # список сложностей каждого задания
        for i in listOfObjectsOfTasks:
            maxScoresOfTasks.append(i.MaxTScore)
            difficultiesOfTasks.append(i.Difficulty)
        sumOfScoresForEachTask = []  # список баллов, суммарно полученных всеми студентами за каждое задание
        meanScoresForEachTask = []  # список средних значений полученных баллов по каждому заданию
        for i in range(len(listOfObjectsOfTasks)):
            meanScoresForEachTask.append(0)
            sumOfScoresForEachTask.append(0)
        for i in range(len(listOfObjectsOfCompletedTasks)):
            count = 0
            for j in listOfObjectsOfCompletedTasks[i]:
                meanScoresForEachTask[count] += j.GetTaskScore
                sumOfScoresForEachTask[count] += j.GetTaskScore
                count += 1
        koef = []
        for i in range(len(meanScoresForEachTask)):
            meanScoresForEachTask[i] /= len(listOfObjectsOfCompletedTasks)
            koef.append(meanScoresForEachTask[i] / maxScoresOfTasks[i])
            Road[listOfObjectsOfTasks[i].Task_Id] = (sumOfScoresForEachTask[i] * koef[i]) / difficultiesOfTasks[i]
        sorted_tuples = sorted(Road.items(), key=lambda item: item[1], reverse=True)
        sorted_road = {k: v for k, v in sorted_tuples}
        sorted_road_list_of_keys = list(sorted_road.keys())
        sorted_road_list_of_keys_task_objects = self.GetListOfTasks(sorted_road_list_of_keys)
        return sorted_road_list_of_keys_task_objects

    def main(self):
        neigh = self.getNeighbors()
        print("Student")
        self.currentStudent.Print()
        print("Neighbors")
        for i in neigh:
            i.Print()
        completedTasks = self.GetCompletedTasks(neigh)
        print("Complted Tasks:")
        for i in completedTasks:
            for j in i:
                j.Print()
        tasks = self.GetTasks(completedTasks)
        print("Tasks:")
        for i in tasks:
            i.Print()
        road = self.GetRoad(completedTasks, tasks)
        print("Road:")
        for i in road:
            print(i.Task_Id)
        return road
