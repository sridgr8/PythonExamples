'''
Created on May 13, 2019

@author: Srinivasulu
'''
from datetime import date
import configparser
executionDate = date.today()
with open("D:\ECLIPSE PROJECTS\TestRepoOne\PythonExamples\\testProp.properties", 'w') as f:
    conf = configparser.ConfigParser()
    conf.set('DEFAULT', 'executiondate', str(executionDate))
    conf.write(f)
