"""
from Filtering import Filterisation
from NumberOfTaskInTest import NumberInTest
"""

class TaskWsDTO:
    def __init__(self, taskQueueInOutput, Theme, taskQueue):
        self.TaskQueueInOutput = taskQueueInOutput
        self.Theme = Theme
        self.TaskQueue = taskQueue
"""
def getTasksWsDTOList(studId, subId, testId):
    newFilter = Filterisation(id=studId, subjectId=subId, testId=testId)
    road = newFilter.main()
    newNumbers = NumberInTest(testId=testId)
    numbers = newNumbers.setgetNumbersInTest()
    tasksWsDtoList = []
    i = 1
    for task in road:
        newTaskWsDto = TaskWsDTO(i, task.Theme, numbers.get(task.Task_Id))
        tasksWsDtoList.append(newTaskWsDto)
        i+=1
    return tasksWsDtoList
"""
def getTaskWsDtoListMock(studId,subId,testId):
    tasksWsDtoList = []
    for i in range(10):
        newTaskWsDto = TaskWsDTO(i,"testTheme", i-1)
        tasksWsDtoList.append(newTaskWsDto)
    return tasksWsDtoList