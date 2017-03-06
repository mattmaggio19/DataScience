import os, datetime , subprocess, pickle
from shutil import copytree , copy


# Root path for rel pathing
Root = r'C:\Users\mattm_000\PycharmProjects\PythonDataAnalysisFramework'
# What virtual env to use
EnvName = r'DefaultData'
Env = os.path.abspath(os.path.join(Root + r'\DefaultDataEnv'))

# Most importantly, what raw data should be brought with us?


# ---- Everything between these lines should be abstracted into a data_project class-------
# Determine a  quasi unique string for creation of the project template. Abstract into general class
# date=datetime.datetime.today() # use if you want to generate a new dir each second (good for iteration)
date = datetime.date.today() # use if you want to generate a new dir each day (good for troubleshooting)
timetup = date.timetuple()

datestr = str(date.year) + str(date.month) + str(date.day) + str(timetup.tm_hour) + str(timetup.tm_min)+ str(timetup.tm_sec)

# string name for project
ProjectName = r'Titanic'
# Generate project pathing
ProjectPath = os.path.abspath(os.path.join(Root + r'\\' + ProjectName + r'\\'+ ProjectName + datestr))

# Create dir for project with unique string of numbers on the end.
if not os.path.exists(ProjectPath):
    os.mkdir(ProjectPath)


# Path to Env folder inside the prj
ProjEnvPath = os.path.abspath(os.path.join(Root + r'\\' + ProjectName + r'\\' + ProjectName + datestr + r'\\' + ProjectName + 'Env' ))
if not os.path.exists(ProjEnvPath):
    copytree(Env, ProjEnvPath)

# Copy the General methods from the path
GeneralClasses = os.path.abspath(os.path.join(Root + r'\\' + r'GeneralClasses'))
GeneralClassesPath = os.path.abspath(os.path.join(ProjectPath + r'\\' + r'GeneralClasses'))
if not os.path.exists(GeneralClassesPath):
    copytree(GeneralClasses, GeneralClassesPath)

# Copy the Custom methods from the path
CustomClasses = os.path.abspath(os.path.join(Root + r'\\' + ProjectName + r'\\' + r'CustomClasses'))
CustomClassesPath = os.path.abspath(os.path.join(ProjectPath + r'\\' + r'CustomClasses'))
if not os.path.exists(CustomClassesPath):
    copytree(CustomClasses, CustomClassesPath)

# Create a copy of the master script from the base folder in the project folder
MasterScript = os.path.abspath(os.path.join(Root + r'\\' + ProjectName + r'\\' + 'MasterFileTemplate.py'))
MasterScriptPath = os.path.abspath(os.path.join(ProjectPath + r'\\' + r'MasterScript.py'))
copy(MasterScript, MasterScriptPath)

# Create a bat script that runs the masterscript from inside the local Env
BatName = 'RunFromEnv.bat'
BatPath = os.path.abspath(os.path.join(ProjectPath + r'\\',  BatName))
Bat = open(BatPath,'w')
BatStr = os.path.abspath(os.path.join(ProjEnvPath + r'\\' + EnvName + r'\\' + 'Scripts' + r'\\' +'python.exe'))
BatStr = BatStr + '  ' + MasterScriptPath
Bat.write(BatStr)
Bat.close()

# Create the spark.py folder that calls the above bat script.
SparkName = 'Spark.py'
SparkPath = os.path.abspath(os.path.join(ProjectPath + r'\\',  SparkName))
Spark = open(SparkPath,'w')
SparkStr = r"""import subprocess;  """
SparkStr = SparkStr + """subprocess.call('"""""
SparkStr = SparkStr + BatPath +"""')"""
Spark.write(SparkStr)
Spark.close()

# Create and save a dict with the absolute paths from this script in case we need to access them again
Dictname = 'PathDict.p'
Dict = {
    'Root': Root,
    'ProjEnvPath': ProjEnvPath,
    'SparkPath': SparkPath,
    'BatPath': BatPath,
    'MasterScriptPath': MasterScriptPath,
    'GeneralClassesPath': GeneralClassesPath,
    'CustomClassesPath':CustomClassesPath
    }

DictPath = os.path.abspath(os.path.join(ProjectPath + r'\\' + Dictname))
pickle.dump(dict, open(DictPath,'wb'))

# Run the spark.py file. This is all the end user should need to do to reproduce the results
# Shell=True is hacky, see if you can fix
subprocess.call('python ' + SparkPath, shell=True)