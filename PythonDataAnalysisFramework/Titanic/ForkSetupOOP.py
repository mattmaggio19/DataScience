from GeneralClasses import Project
import subprocess

#Init Project
Root = r'C:\Users\mattm_000\PycharmProjects\PythonDataAnalysisFramework'
PrjName = 'Titanic'
Env = r'DefaultData'
Data = r'Data\Titanic_dataset'
Master = PrjName + '\\' + 'MasterFileTemplate.py'
GeneralClass = r'GeneralClasses'
CustomClasses = r'CustomClasses'

#init the project
prj = Project.Project(PrjName, Root, Env, Data, Master, GeneralClass, CustomClasses)

#Create the dir
prj.CreateDir()

#Copy in the necessary information
prj.FetchInfoToProject()

#Save the prj object
prj.SaveToWorkingDir()

#Run the analysis (only code necessary to reproduce results)

