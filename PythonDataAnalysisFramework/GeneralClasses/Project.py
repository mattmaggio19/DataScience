import os, datetime , subprocess, pickle
from shutil import copytree , copy

class Project(object):
    def __init__(self, name, root, env, data , master, generalclasses, customclasses):
        #pathing strings that define the project activities. Paths should be rel from root
        self.name = name
        self.root = root
        self.env = env
        self.dataSource = data
        self.masterSource = master
        self.generalclasses = generalclasses
        self.customclasses = customclasses
        #Init default values
        self.SetBigData(False)
        self.MinSec = False
        self.UseCustomEnv = False


    def SetBigData(self, BigData):
        self.BigData = BigData

    def CreateDir(self):
        self.DateTimeString = self.GenDateTimeString()
        self.ProjectPath = os.path.abspath(os.path.join(self.root + r'\\' + self.name + r'\\'+ self.name + self.DateTimeString))
        if not os.path.exists(self.ProjectPath):
            os.mkdir(self.ProjectPath)

    def GenDateTimeString(self):
        date = datetime.datetime.today()
        timetup = date.timetuple()
        # Make date an month readable with 0s in the name instead of 34 being march third
        if len(str(date.month)) < 2:
            month = str(0) + str(date.month)
        else:
            month = str(date.month)
        if len(str(date.day)) < 2:
            day = str(0) + str(date.day)
        else:
            day = str(date.day)
        if self.MinSec == True:
            return str(date.year) + str(month) + str(day) + str(timetup.tm_hour) + str(timetup.tm_min) + str(timetup.tm_sec)
        else:
            return str(date.year) + str(month) + str(day)


    def FetchInfoToProject(self):

        # Copy the General methods from the path
        print self.root
        General = self.CreatePath(self, self.root, self.generalclasses)
        GeneralPath = self.CreatePath(self, self.ProjectPath, self.generalclasses)

        if not os.path.exists(GeneralPath):
            copytree(General, GeneralPath)

    def CreatePath(self, root, *args):
        print root
        str = root + r'\\'
        for arg in args:
            str + arg + r'\\'
        return os.path.abspath(str)


    def SaveToWorkingDir(self):
        pass

    def LoadFromWorkingDir(self):
        pass

    def ExecuteAnalysis(selfs):
        pass